using System;

Console.Write("N: ");
int N = Convert.ToInt32(Console.ReadLine());
for (int i = 1; i <= N; i++)
{
    int maxdigits = 0;
    int max = N * N;
    while (max > 0)
    {
        max /= 10;
        maxdigits++;
    }
    for (int j = 1; j <= N; j++)
    {
        int mult = i * j;
        int digits = 0;
        while (mult > 0)
        {
            mult /= 10;
            digits++;
        }
        for (int x = 1; x <= (maxdigits - digits); x++)
        {
            Console.Write(" ");
        }
        Console.Write(" ");
        Console.Write(i * j);
    }
    Console.WriteLine();
}