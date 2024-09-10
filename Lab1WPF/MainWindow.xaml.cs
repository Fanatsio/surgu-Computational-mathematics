using LiveChartsCore;
using LiveChartsCore.SkiaSharpView;

namespace Lab1WPF
{
    public class ViewModel
    {
        static double Function(double x)
        {
            return x + 2 * Math.Sin(x) + Math.Cos(3 * x);
        }

        public static (double[] xValues, double[] yValues) GenerateData()
        {
            const double start = -10.0;
            const double end = 20.0;
            const double step = 0.1;

            int count = (int)((end - start) / step) + 1;
            var xValues = new double[count];
            var yValues = new double[count];

            for (int i = 0; i < count; i++)
            {
                double x = start + i * step;
                xValues[i] = x;
                yValues[i] = Function(x);
            }

            return (xValues, yValues);
        }

        public ISeries[] Series { get; set; }

        public ViewModel()
        {
            var (xValues, yValues) = GenerateData();

            Series = new ISeries[]
            {
                new LineSeries<double>
                {
                    Values = yValues,
                    Fill = null,
                    GeometrySize = 0,
                    LineSmoothness = 1
                }
            };
        }
    }
}
