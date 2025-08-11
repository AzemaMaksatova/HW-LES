const int LDR_PIN = A0;
const int POT_PIN = A1;
const int LED_PIN = 9;
const int BUZZER_PIN = 10;

const long DARK_DURATION = 5000;

unsigned long darkStartTime = 0;
bool isDark = false;             

void setup() {
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  Serial.begin(9600); 
}

void loop() {
  unsigned long currentMillis = millis(); 

  int ldrValue = analogRead(LDR_PIN);
  int potValue = analogRead(POT_PIN);
  
  int threshold = map(potValue, 0, 1023, 200, 400); 

  if (ldrValue < threshold) { 
    
    digitalWrite(LED_PIN, HIGH);
    
    if (!isDark) {
      isDark = true;
      darkStartTime = currentMillis;
    }
    
    if (currentMillis - darkStartTime >= DARK_DURATION) {
      tone(BUZZER_PIN, 1000, 300); 
    } else {
      noTone(BUZZER_PIN);
    }

  } else {
    digitalWrite(LED_PIN, LOW); 
    noTone(BUZZER_PIN);        
    isDark = false;
    darkStartTime = 0;
  }

 
  
  delay(50);
}