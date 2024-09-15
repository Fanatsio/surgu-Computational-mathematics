using LiveChartsCore;
using LiveChartsCore.SkiaSharpView;

namespace Lab1WPF
{
    public class ViewModel
    {
        public ISeries[] Series { get; private set; }

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

        private static (double[] xValues, double[] yValues) GenerateData()
        {
            const double Start = -10.0;
            const double End = 20.0;
            const double Step = 0.1;
            const int Count = (int)((End - Start) / Step) + 1;

            var xValues = new double[Count];
            var yValues = new double[Count];

            for (int i = 0; i < Count; i++)
            {
                double x = Start + i * Step;
                xValues[i] = x;
                yValues[i] = CalculateFunction(x);
            }

            return (xValues, yValues);
        }

        private static double CalculateFunction(double x)
        {
            return x + 2 * Math.Sin(x) + Math.Cos(3 * x);
        }
    }
}