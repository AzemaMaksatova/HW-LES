const int trigPin = 9;
const int echoPin = 10;
const int buzzerPin = 11;
const int ledPin = 12;

const int distanceThreshold = 50;

long duration;
int distanceCm;

const int blinkCycles = 5;
const int blinkDelay = 200;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distanceCm = duration * 0.0343 / 2;


  if (distanceCm < distanceThreshold) {

    for (int i = 0; i < blinkCycles; i++) {
      digitalWrite(ledPin, HIGH);
      tone(buzzerPin, 1500);
      delay(blinkDelay);

      noTone(buzzerPin);
      digitalWrite(ledPin, LOW);
      delay(blinkDelay);
    }
    
    delay(500);
    
  } else {
    digitalWrite(ledPin, LOW);
    noTone(buzzerPin);
  }
  delay(100);
}