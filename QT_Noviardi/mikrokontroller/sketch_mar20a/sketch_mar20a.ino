#define led 3
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led, OUTPUT);

}

// fungsi membaca perintah dari serial python
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>1){
    String data_perintah = Serial.readString();
    Serial.println(data_perintah);
    if (data_perintah=="on"){
      digitalWrite(led, HIGH);
      //nyalakan led
    }
    else if(data_perintah=="off"){
      digitalWrite(led, LOW);
      //matikan led
    }
  }

}
