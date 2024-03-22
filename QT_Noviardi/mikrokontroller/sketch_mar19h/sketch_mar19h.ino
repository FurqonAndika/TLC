#define led 3
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
    String data = Serial.readStringUntil('\n');
    Serial.println(data);
    if(data=="on"){
      digitalWrite(led, HIGH);
    }
    else if(data=="off"){
      digitalWrite(led, LOW);
    }

  }

}
