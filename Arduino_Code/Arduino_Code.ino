String data;
char d1;
void setup() 
{
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  print_off();
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop()
{
  if(Serial.available())
  {
    data = Serial.readString();
    d1 = data.charAt(0);
    if(d1 == '0')
    {
      print_zero();
    }
    else if (d1 == '1')
    {
      print_one();
    }
    else if (d1 == '2')
    {
      print_two();
    }
    else if (d1 == '3')
    {
      print_three();
    }
    else if (d1 == '4')
    {
      print_four();
    }
    else if (d1 == '5')
    {
      print_five();
    }
    else if (d1 == '6')
    {
      print_six();
    }
    else if (d1 == '7')
    {
      print_seven();
    }
    else if (d1 == '8')
    {
      print_eight();
    }
    else if (d1 == '9')
    {
      print_nine();
    }
  }
}
