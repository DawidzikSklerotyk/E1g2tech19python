using System.Xml.Serialization;

// zad 1
int a = int.Parse(Console.ReadLine());
int b = int.Parse(Console.ReadLine());

if ((a + b) % 2 == 0)
{
    Console.WriteLine("TAK");
}
else
    Console.WriteLine("NIE");
// zad 2
int c = int.Parse(Console.ReadLine());
int d = int.Parse(Console.ReadLine());
if ((c + d) / 2 > Math.Sqrt(c + d))
{
    Console.WriteLine("TAK");
}
else
    Console.WriteLine("NIE");
// zad 3
int e = int.Parse(Console.ReadLine());
int f = int.Parse(Console.ReadLine());
int g = int.Parse(Console.ReadLine());

if (e == f || e == g)
{
    Console.WriteLine(e);
}
else if (g == f)
{
    Console.WriteLine(g);
}
// zad 4
int h = int.Parse(Console.ReadLine());
int i = int.Parse(Console.ReadLine());
int j = int.Parse(Console.ReadLine());
int k = int.Parse(Console.ReadLine());

if (h < i && j && k)
{
    Console.WriteLine(h);
}
else if (i < h && j && k)
{
    Console.WriteLine(i);
}
else if (j < h && i && k)
{
    Console.WriteLine(j);
}
else if (k < i && j && h)
{
    Console.WriteLine(k);
}
// zad 5
int l = int.Parse(Console.ReadLine());
int m = int.Parse(Console.ReadLine());
int o = int.Parse(Console.ReadLine());

if (l < m + o || m < l + o || o < m + l)
{
    Console.WriteLine("TAK");
}
else
    Console.WriteLine("NIE");
// zad 6
Console.WriteLine("Podaj kąty trójkątów");
int p = int.Parse(Console.ReadLine());
int r = int.Parse(Console.ReadLine());
int s = int.Parse(Console.ReadLine());

if (p < 90 && r < 90 && s < 90)
{
    Console.WriteLine("ostrokątny");
} 
    
else if (p == 90 || s == 90 || r == 90)
{
    Console.WriteLine("prostokątny");
}
else if (p > 90 || s > 90 || r > 90)
{
    Console.WriteLine("rozwartokątny");
}
