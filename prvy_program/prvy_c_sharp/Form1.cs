using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prvy_c_sharp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            float prve = Convert.ToInt32( textBox1.Text);
            float druhe = Convert.ToInt32(textBox2.Text);

            float vysledok = prve / druhe;

            MessageBox.Show(Convert.ToString(vysledok));
        }
    }
}
