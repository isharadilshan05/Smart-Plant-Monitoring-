int sensorPin = A0;
int relayPin = 7;

void setup() {
  Serial.begin(9600);
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW); // relay OFF
}

void loop() {

  // Check for commands from Raspberry Pi
  if (Serial.available()) {
    char cmd = Serial.read();

    if (cmd == '1') {
      digitalWrite(relayPin, HIGH);   // Relay ON
    }
    else if (cmd == '0') {
      digitalWrite(relayPin, LOW);    // Relay OFF
    }
  }

  // Read moisture sensor
  int moisture = analogRead(sensorPin);
  Serial.println(moisture);

  delay(500);
}
