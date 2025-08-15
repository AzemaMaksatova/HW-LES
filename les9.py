const int trigPin = 9;
const int echoPin = 10;
const int buzzerPin = 8;

const int redPin = 7;
const int greenPin = 5; 
const int bluePin = 6; 

long duration;
int distance;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  
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

  digitalWrite(redPin, LOW);
  digitalWrite(greenPin, LOW);
  digitalWrite(bluePin, LOW);
  noTone(buzzerPin);
  
  if (distance > 30) {
    digitalWrite(greenPin, HIGH);
  } else if (distance <= 30 && distance > 15) {
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, HIGH);
    tone(buzzerPin, 1500); 
  } else if (distance > 5) {
    digitalWrite(redPin, HIGH);
    tone(buzzerPin, 2500);
  } else { 
    digitalWrite(redPin, HIGH);
    tone(buzzerPin, 3000); 
  }
  
  delay(500); 
}