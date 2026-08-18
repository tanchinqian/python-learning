

string[] names = ["Sophia", "Nicolas" , "Zahirah" , "Jeong"];
double[] avg = new double[5] ;


int[,] studentGrades =
{
  {93, 87 , 98 , 95 , 100},// Sophia
  {80, 83 , 82 , 88 , 85},//Nicolas
  {84 , 96 , 73 , 85 , 79},//Zahirah
  {90 , 92 , 98, 100 , 97}//Jeong
};

for(int i = 0 ; i < studentGrades.GetLength(0) ; i++)
{
  int sum = 0 ;  
  for(int j = 0 ; j < studentGrades.GetLength(1) ; j++)
  {
    sum += studentGrades[i,j];
  }
  avg[i] = (float)(sum/ 5.0m);
}
Console.WriteLine("Student\t\tGrade");

for ( int i = 0 ; i < 4 ; i++)
{
  Console.WriteLine($"{names[i]}\t\t{avg[i].ToString("0.0")}\t{ ((avg[i] > 90)? 'A' : 'B')}");
}