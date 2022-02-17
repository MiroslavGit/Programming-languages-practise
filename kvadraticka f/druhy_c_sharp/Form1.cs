using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace druhy_c_sharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int a = Convert.ToInt32(textBox1.Text);
            int b = Convert.ToInt32(textBox2.Text);
            int c = Convert.ToInt32(textBox3.Text);

            textBox4.Text=("Tvoja rovnica : " + Convert.ToString(a) +"x*x + " + Convert.ToString(b) + " x + " + Convert.ToString(c));


            int D = b * b - 4 * a * c;

            if (D < 0) {
                textBox5.Text = ("Rovnica nemá riešenie");
                }
            else if(D == 0) {
                textBox4.Text = ("Rovnica má jedno riešenie");
                float x1 = -b / 2 * a;
                textBox5.Text = ("X1 je:"+ Math.Round((x1)));
        }
            else {
                double odmocninaD = Math.Round(Math.Sqrt(D),2);
                textBox4.Text = ("Odmocnina s diskriminantu je:"+ odmocninaD);
                double x1 = (-b - odmocninaD) / 2 * a;
                double x2 = (-b + odmocninaD) / 2 * a;
                textBox5.Text = ("X1 je:" + Math.Round(x1)+ " X2 je: "+ Math.Round(x2));
            }








        }
    }
}
