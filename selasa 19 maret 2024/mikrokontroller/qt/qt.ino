void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}
int rpm, kecepatan, voltage, current, engine_temp, temp;
void loop() {
  // put your main code here, to run repeatedly:
  rpm +=1;
  if(rpm>100)rpm=0;
  kecepatan +=1;
  if (kecepatan>200)kecepatan=0;
  String data="";
  data = "data=";
  data +=String(rpm);
  data +=",";
  data +=String(kecepatan);
  data +=",220,";
  data +="10,";
  data +="200,";
  data +="100";
  
  
  
  Serial.println(data);
}
