void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  int speed = random(0, 180);
  int rpm = random(0, 6000);
  int engine_temp = random(0, 300);
  int temp = random(0, 30);
  int current = random(0, 10);
  int voltage = random(10, 144);

  String data = "";
  data += String(speed)+",";
  data += String(rpm)+",";
  data += String(engine_temp)+",";
  data += String(temp)+",";
  data += String(current)+",";
  data += String(voltage)+",";
  
  Serial.println(data);


}
