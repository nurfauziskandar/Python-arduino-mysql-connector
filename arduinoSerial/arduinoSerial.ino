void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print("data1");
  Serial.print(", ");
  Serial.print("data2");
  Serial.print(", ");
  Serial.print("data3");
  Serial.print(", ");
  Serial.print("data4");
  Serial.print(", ");
  Serial.print("data5");
  Serial.print(", ");
  Serial.print("data6");
  Serial.print(", ");
  Serial.println("data7");
}
