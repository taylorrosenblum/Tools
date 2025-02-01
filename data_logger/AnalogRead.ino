const int piezoPin = A0; // Analog pin connected to the piezo sensor
int reading = 0;

void setup() {
  Serial.begin(9600);
}
void loop() {
    reading = analogRead(piezoPin);
    Serial.println(reading);
}
