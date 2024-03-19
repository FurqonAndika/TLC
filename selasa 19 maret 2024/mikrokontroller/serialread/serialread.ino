//serialread
#define led 3


void setup(){
  Serial.begin(9600);
  pinMode(led, OUTPUT);

}
void loop(){
  if (Serial.available()>0){
    String data = Serial.readStringUntil('\n');
    Serial.println(data);
    if (data=="on"){
      digitalWrite(led, HIGH);
    }
    else if(data=="off"){
      digitalWrite(led, LOW);
    }
  }
}
