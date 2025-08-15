const int BUZZER_PIN = 9;
const int LED_PIN = 13;
const int FSR_PIN = A0;

const int threshold = 200;

int melody[] = { 262, 294, 330, 349, 392, 440, 494 };
const int noteDuration = 250;
const int numNotes = sizeof(melody) / sizeof(melody[0]);

int fsrReading = 0;

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  fsrReading = analogRead(FSR_PIN);

  if (fsrReading > threshold) {
    playMelody();
    flashLED();
    delay(50);
  } else {
    digitalWrite(LED_PIN, LOW);
    noTone(BUZZER_PIN);
  }
}

void playMelody() {
  for (int i = 0; i < numNotes; i++) {
    tone(BUZZER_PIN, melody[i], noteDuration);
    delay(noteDuration + 20);
    noTone(BUZZER_PIN);
  }
}

void flashLED() {
  digitalWrite(LED_PIN, HIGH);
}