const int ledPin = 2;
char command;

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    command = Serial.read();
    if (command == 'T') {
      // Toggle the state of the LED
      digitalWrite(ledPin, !digitalRead(ledPin));
    }
  }
}
