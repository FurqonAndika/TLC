// serial communication
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("hello world");

}
void myfunction(){
  Serial.println("hello 1111111111111111111");
}

unsigned long waktu_awal = 0;

unsigned long waktu_sekarang = 0;
void loop() {
  // put your main code here, to run repeatedly:
  // Serial.println(millis()); //timer 32 bit
  waktu_sekarang = millis();
  if (waktu_sekarang-waktu_awal>1000){
    myfunction();
    waktu_awal=waktu_sekarang;
  }
  Serial.println("fungsi");
}