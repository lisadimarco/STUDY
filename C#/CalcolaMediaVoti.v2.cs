using System;

public class Media
{
    // Dichiarazione degli array come membri della classe
    private string[] nomi = new string[4];
    private int[] voto1 = new int[4];
    private int[] voto2 = new int[4];
    private int[] voto3 = new int[4];
    private int[] voto4 = new int[4];
    private double[] medie = new double[4]; // Tipo corretto per memorizzare la media

    // Metodo per inserire i nomi
    public void InserireNomi()
    {
        for (int i = 0; i < nomi.Length; i++)
        {
            Console.Write($"Inserisci il nome del {i + 1}° studente: ");
            nomi[i] = Console.ReadLine();
        }

        Console.WriteLine("\nHai inserito i seguenti nomi:");
        foreach (string nome in nomi)
        {
            Console.WriteLine(nome);
        }
    }

    // Metodo per inserire i voti
    public void InserireVoti()
    {
        for (int i = 0; i < nomi.Length; i++)
        {
            Console.WriteLine($"\nInserisci i voti per {nomi[i]}:");

            Console.Write("Voto 1: ");
            voto1[i] = int.Parse(Console.ReadLine());

            Console.Write("Voto 2: ");
            voto2[i] = int.Parse(Console.ReadLine());

            Console.Write("Voto 3: ");
            voto3[i] = int.Parse(Console.ReadLine());

            Console.Write("Voto 4: ");
            voto4[i] = int.Parse(Console.ReadLine());
        }
    }

    // Metodo per calcolare la media dei voti
    public void CalcoloMedia()
    {
        for (int i = 0; i < nomi.Length; i++)
        {
            medie[i] = (voto1[i] + voto2[i] + voto3[i] + voto4[i]) / 4.0; // Divisione decimale
        }

        Console.WriteLine("\nLe medie dei voti sono:");
        for (int i = 0; i < nomi.Length; i++)
        {
            Console.WriteLine($"{nomi[i]}: {medie[i]:F2}");
        }
    }

    // Metodo per ottenere la valutazione in base al voto
    public string Valutazione(int voto)
    {
        if (voto >= 97 && voto <= 100) return "A+";
        if (voto >= 93 && voto <= 96) return "A";
        if (voto >= 90 && voto <= 92) return "A-";
        if (voto >= 87 && voto <= 89) return "B+";
        if (voto >= 83 && voto <= 86) return "B";
        if (voto >= 80 && voto <= 82) return "B-";
        if (voto >= 77 && voto <= 79) return "C+";
        if (voto >= 73 && voto <= 76) return "C";
        if (voto >= 70 && voto <= 72) return "C-";
        if (voto >= 67 && voto <= 69) return "D+";
        if (voto >= 63 && voto <= 66) return "D";
        if (voto >= 60 && voto <= 62) return "D-";
        if (voto >= 0 && voto <= 59) return "F";
        return "Valore non valido";
    }

    // Metodo per stampare valutazioni
    public void StampaValutazioni()
    {
        Console.WriteLine("\nValutazioni dei voti:");
        for (int i = 0; i < nomi.Length; i++)
        {
            Console.WriteLine($"\nValutazioni per {nomi[i]}:");
            Console.WriteLine($"Voto 1: {voto1[i]} - {Valutazione(voto1[i])}");
            Console.WriteLine($"Voto 2: {voto2[i]} - {Valutazione(voto2[i])}");
            Console.WriteLine($"Voto 3: {voto3[i]} - {Valutazione(voto3[i])}");
            Console.WriteLine($"Voto 4: {voto4[i]} - {Valutazione(voto4[i])}");
        }
    }
}

// Esempio di utilizzo
class Program
{
    static void Main(string[] args)
    {
        Media media = new Media();
        media.InserireNomi();
        media.InserireVoti();
        media.CalcoloMedia();
        media.StampaValutazioni();
    }
}



  
