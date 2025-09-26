#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include <Servo.h>

LiquidCrystal_I2C lcd(0x27, 16, 2); 

Servo myservo; 

const int GAS_PIN = A2;      
const int MOVEMENT_PIN = 13;  
const int LIGHT_PIN = A2;    
const int BUZZER_PIN = 4;    
const int MOISTURE_PIN = A3; 

const int GAS_THRESHOLD = 300; 
const int LIGHT_THRESHOLD = 500; 
const int MOISTURE_THRESHOLD = 700; 

void setup() {
  Serial.begin(9600);
  
  pinMode(MOVEMENT_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  
  lcd.init(); 
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Smart Kitchen");
  lcd.setCursor(0, 1);
  lcd.print("Ready...");
  
  myservo.attach(9); 
  myservo.write(0); 
  
  delay(2000);
  lcd.clear();
}

void loop() {
  int gasValue = analogRead(GAS_PIN);
  int movementState = digitalRead(MOVEMENT_PIN);
  int lightValue = analogRead(LIGHT_PIN);
  int moistureValue = analogRead(MOISTURE_PIN);

  bool isGasLeak = gasValue > GAS_THRESHOLD;
  bool isMovement = movementState == HIGH;
  bool isDark = lightValue < LIGHT_THRESHOLD;
  bool isLeak = moistureValue > MOISTURE_THRESHOLD; 

  if (isGasLeakisLeak) {
    handleAlarm(isGasLeak, isMovement, isLeak);
  } else {
    digitalWrite(BUZZER_PIN, LOW); 
  }

  if (!isDark) {
    myservo.write(90); 
  } else {
    myservo.write(0);  
  }

  updateDisplay(isGasLeak, isMovement, isDark, isLeak);
  printDebug(gasValue, lightValue, moistureValue);

  delay(500); 
}

void handleAlarm(bool gas, bool movement, bool leak) {
  digitalWrite(BUZZER_PIN, HIGH);
  
  Serial.print("!!! TREVOGA: ");
  if (gas) Serial.print("GAZ ");
  if (movement) Serial.print("DVIZHENIE ");
  if (leak) Serial.print("UTECHKA ");
  Serial.println("!!!");
}

void updateDisplay(bool gas, bool movement, bool dark, bool leak) {
  lcd.setCursor(0, 0);
  lcd.print("G:");
  lcd.print(gas ? "!!! " : "OK  ");
  lcd.print("D:");
  lcd.print(movement ? "YES " : "NO  ");
  
  lcd.setCursor(0, 1);
  lcd.print("L:");
  lcd.print(dark ? "DARK" : "LITE");
  lcd.print(" U:");
  lcd.print(leak ? "!!! " : "OK  ");
}

void printDebug(int gas, int light, int moisture) {
  Serial.print("Gas:");
  Serial.print(gas);
  Serial.print(" | Light:");
  Serial.print(light);
  Serial.print(" | Moisture:");
  Serial.println(moisture);
}
