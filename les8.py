const int trigPin = 9;
const int echoPin = 10;
const int greenLed = 5;
const int yellowLed = 6;
const int redLed = 7;
const int buzzerPin = 8;

long duration;
int distance;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(greenLed, OUTPUT);
  pinMode(yellowLed, OUTPUT);
  pinMode(redLed, OUTPUT);
  pinMode(buzzerPin, OUTPUT);

  Serial.begin(9600); 
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);

  distance = duration * 0.034 / 2;

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  digitalWrite(greenLed, LOW);
  digitalWrite(yellowLed, LOW);
  digitalWrite(redLed, LOW);
  noTone(buzzerPin);
  
  if (distance > 30) {
    digitalWrite(greenLed, HIGH);
  
  } else if (distance <= 30 && distance > 15) {
    digitalWrite(yellowLed, HIGH);
    tone(buzzerPin, 1500);
  } else if (distance > 5) {
    digitalWrite(redLed, HIGH);
    tone(buzzerPin, 2500);
  } else { 
    digitalWrite(redLed, HIGH);
    tone(buzzerPin, 3000); 
  }
  
  delay(500); 
}