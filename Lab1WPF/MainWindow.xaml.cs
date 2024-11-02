using CommunityToolkit.Mvvm.ComponentModel;
using LiveChartsCore;
using LiveChartsCore.Defaults;
using LiveChartsCore.SkiaSharpView;
using System.IO;

namespace Lab1WPF
{
    public partial class ViewModel : ObservableObject
    {
        public ISeries[] Series { get; set; }

        public ViewModel()
        {
            var points = GenerateData();

            Series = new ISeries[]
            {
                new LineSeries<ObservablePoint>
                {
                    Values = points,
                    Fill = null,
                    GeometrySize = 0,
                    LineSmoothness = 1
                }
            };
        }

        private static ObservablePoint[] GenerateData()
        {
            const double Start = -10.0;
            const double End = 20.0;
            const double Step = 0.1;

            int count = (int)((End - Start) / Step) + 1;

            var points = new ObservablePoint[count];

            string[] dataLines = new string[count + 1];
            dataLines[0] = "x,y";

            for (int i = 0; i < count; i++)
            {
                double x = Start + i * Step;
                double y = CalculateFunction(x);

                points[i] = new ObservablePoint(x, y);

                dataLines[i + 1] = $"{x},{y}";
            }

            ExportDataToFile(dataLines);

            return points;
        }

        private static double CalculateFunction(double x)
        {
            return x + 2 * Math.Sin(x) + Math.Cos(3 * x);
        }

        private static void ExportDataToFile(string[] dataLines)
        {
            string filePath = "exported_data.csv";

            try
            {
                File.WriteAllLines(filePath, dataLines);
                Console.WriteLine($"Данные успешно сохранены в {filePath}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Ошибка при записи данных в файл: {ex.Message}");
            }
        }
    }
}