using System;
using System.Collections.Generic;

namespace Baekjoon
{
    class Program
    {
        static int n, m;
        abstract class Piece
        {
            public int x, y;
            public Piece(int a, int b)
            {
                x = a;
                y = b;
            }
            public abstract void check(Piece[,] board, bool[,] ans);
        }
        class Queen : Piece
        {
            public Queen(int a, int b) : base(a, b) { }
            public override void check(Piece[,] board, bool[,] ans)
            {
                ans[x, y] = true;
                int[] Qx = { -1, -1, -1, 0, 0, 1, 1, 1 };
                int[] Qy = { -1, 0, 1, -1, 1, -1, 0, 1 };

                for (int i = 0; i < 8; i++)
                {
                    int tempx = x + Qx[i];
                    int tempy = y + Qy[i];
                    while (tempx >= 0 && tempy >= 0 && tempx < n && tempy < m)
                    {
                        if (board[tempx, tempy] != null) break;
                        ans[tempx, tempy] = true;
                        tempx += Qx[i];
                        tempy += Qy[i];
                    }
                }
            }
        }
        class Knight : Piece
        {
            public Knight(int a, int b) : base(a, b) { }
            public override void check(Piece[,] board, bool[,] ans)
            {
                ans[x, y] = true;
                if (x - 1 >= 0)
                {
                    if (y - 2 >= 0) ans[x - 1, y - 2] = true;
                    if (y + 2 < m) ans[x - 1, y + 2] = true;
                    if (x - 2 >= 0)
                    {
                        if (y - 1 >= 0) ans[x - 2, y - 1] = true;
                        if (y + 1 < m) ans[x - 2, y + 1] = true;
                    }
                }
                if (x + 1 < n)
                {
                    if (y - 2 >= 0) ans[x + 1, y - 2] = true;
                    if (y + 2 < m) ans[x + 1, y + 2] = true;
                    if (x + 2 < n)
                    {
                        if (y - 1 >= 0) ans[x + 2, y - 1] = true;
                        if (y + 1 < m) ans[x + 2, y + 1] = true;
                    }
                }
            }
        }
        class Pawn: Piece
        {
            public Pawn(int a, int b) : base(a, b) { }
            public override void check(Piece[,] board, bool[,] ans)
            {
                ans[x, y] = true;
            }
        }
        static void Main(string[] args)
        {
            List<Pawn> pawns = new List<Pawn>();
            List<Knight> knights = new List<Knight>();
            List<Queen> queens = new List<Queen>();

            string[] arr = Console.ReadLine().Split();
            n = int.Parse(arr[0]);
            m = int.Parse(arr[1]);
            Piece[, ] board = new Piece[n, m];
            bool[,] ans = new bool[n, m];

            arr = Console.ReadLine().Split();
            int temp = int.Parse(arr[0]);
            for (int i = 1; i < temp + 1; i++)
            {
                int r = int.Parse(arr[i * 2 - 1]) - 1;
                int c = int.Parse(arr[i * 2]) - 1;
                Queen q = new Queen(r, c);
                board[r, c] = q;
                queens.Add(q);
            }
            arr = Console.ReadLine().Split();
            temp = int.Parse(arr[0]);
            for (int i = 1; i <= temp; i++)
            {
                int r = int.Parse(arr[i * 2 - 1]) - 1;
                int c = int.Parse(arr[i * 2]) - 1;
                Knight k = new Knight(r, c);
                board[r, c] = k;
                knights.Add(k);
            }
            arr = Console.ReadLine().Split();
            temp = int.Parse(arr[0]);
            for (int i = 1; i <= temp; i++)
            {
                int r = int.Parse(arr[i * 2 - 1]) - 1;
                int c = int.Parse(arr[i * 2]) - 1;
                Pawn p = new Pawn(r, c);
                board[r, c] = p;
                pawns.Add(p);
            }

            foreach (Queen q in queens)
            {
                q.check(board, ans);
            }
            foreach (Knight k in knights)
            {
                k.check(board, ans);
            }
            foreach (Pawn p in pawns)
            {
                p.check(board, ans);
            }

            int cnt = 0;
            for(int i = 0; i < n; i++)
            {
                for(int j = 0; j < m; j++)
                {
                    if (ans[i, j] == false) cnt++;
                }
            }
            Console.WriteLine(cnt);
        }
    }
}
