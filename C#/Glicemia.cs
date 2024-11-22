using System;

public class Glucose
{
    Private Random random;
    public int GlucoseLevel { get; private set; }
    public int[] GlucoseHistory;
    private int index;

  
    public Glucose()
    {
      random = new Random();
    }

  public void CheckGlucoseLevel()
  {
    GlucoseLevel = random.Next(40, 401);
  }
  
  if (glucoseLevel < 70)
  {
      Console.WriteLine("Hypoglicemia");
  }
  else if (glucoseLevel <= 140 && glucoseLevel >= 70)
  {
      Console.WriteLine("Normal Range");
  }
  else if (glucoseLevel > 140 && glucoseLevel <= 200)
  {
      Console.WriteLine("High blood glucose");
  }
  else
  {
      Console.WriteLine("Hyperglicemia");
  }

Console.WriteLine($"Current blood glucose level: {glucoseLevel} mg/dL);
