#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x3F, 16, 2); 

const int tempPin = A0;
const int ldrPin = A1;
const int potPin = A2;
const int ledPin = 13;
const int buzzerPin = 11;

const int LIGHT_THRESHOLD = 300;

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Alarm System Init");
  
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int tempValueRaw = analogRead(tempPin);
  int lightValue = analogRead(ldrPin);
  int potValue = analogRead(potPin);

  float adjustableTempThreshold = map(potValue, 0, 1023, 150, 400) / 10.0;
  
  float voltage = tempValueRaw * 5.0 / 1023.0;
  float tempC = (voltage - 0.5) * 100.0; 

  lcd.setCursor(0, 0);
  lcd.print("T:");
  lcd.print(tempC, 1);
  lcd.print(" T_th:");
  lcd.print(adjustableTempThreshold, 1);

  lcd.setCursor(0, 1);
  lcd.print("L:");
  lcd.print(lightValue);
  lcd.print(" Status: ");

  if (tempC > adjustableTempThreshold || lightValue < LIGHT_THRESHOLD) {
    digitalWrite(ledPin, HIGH);
    digitalWrite(buzzerPin, HIGH);
    
    lcd.print("ALARM!");
    Serial.println("!!! ALARM !!!");
  } else {
    digitalWrite(ledPin, LOW);
    digitalWrite(buzzerPin, LOW);
    
    lcd.print("OK      "); 
    Serial.println("Status: OK");
  }

  delay(500);
}