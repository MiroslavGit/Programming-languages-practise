using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace treti_c_sharp
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

            double vysledok = a % b;

            if (vysledok == 0)
            {
                textBox3.Text = ("Číslo "+Convert.ToString(a)+ " je deliteľné číslom " + Convert.ToString(b));
            }
            else
            {
                textBox3.Text = ("Číslo " + Convert.ToString(a) + " nie je deliteľné číslom " + Convert.ToString(b));
            }
        }
    }
}
