import java.awt.EventQueue;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.LineBorder;
import java.awt.Color;
import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JTextField;
import javax.swing.JTabbedPane;
import javax.swing.SwingConstants;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JSeparator;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Restaurant {

	private JFrame frame;
	private JTextField txtDisplay;
	private JButton btnr;
	private JButton btnC;
	private JButton btnmod;
	private JButton btna;
	private JButton btn7;
	private JButton btn8;
	private JButton btn9;
	private JButton btns;
	private JButton btn4;
	private JButton btn5;
	private JButton btn6;
	private JButton btnm;
	private JButton btn1;
	private JButton btn2;
	private JButton btn3;
	private JButton btnd;
	private JButton btn0;
	private JButton btndot;
	private JButton btn;
	private JButton btneql;
	double firstnum;
	double secondnum;
	double result;
	String operations;
	String answer;
	private JTextField jburger;
	private JTextField jcheese;
	private JTextField jpizza;
	private JTextField jcheesepizza;
	private JTextField jbiryani;
	private JTextField jcoke;
	private JTextField jcoffee;
	private JTextField jbanana;
	private JTextField jlimca;
	private JTextField jshake;
	private JTextField textField_6;
	double nburger;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Restaurant window = new Restaurant();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the application.
	 */
	public Restaurant() {
		initialize();
	}

	/**
	 * Initialize the contents of the frame.
	 */
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(0, 0, 1368, 689);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.getContentPane().setLayout(null);
		
		JPanel panel = new JPanel();
		panel.setBorder(new LineBorder(new Color(0, 0, 0), 8));
		panel.setBounds(36, 149, 524, 218);
		frame.getContentPane().add(panel);
		panel.setLayout(null);
		
		JLabel lblCheeseBurger = new JLabel("Burger");
		lblCheeseBurger.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblCheeseBurger.setBounds(40, 47, 147, 29);
		panel.add(lblCheeseBurger);
		
		JLabel lblCheeseBurger_1 = new JLabel("Cheese Burger");
		lblCheeseBurger_1.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblCheeseBurger_1.setBounds(40, 81, 147, 29);
		panel.add(lblCheeseBurger_1);
		
		JLabel lblVegPizza = new JLabel("Veg Pizza");
		lblVegPizza.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblVegPizza.setBounds(40, 116, 147, 29);
		panel.add(lblVegPizza);
		
		JLabel lblCheesePizza = new JLabel("Cheese Pizza");
		lblCheesePizza.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblCheesePizza.setBounds(40, 148, 147, 29);
		panel.add(lblCheesePizza);
		
		JLabel lblVegBiryani = new JLabel("Veg Biryani");
		lblVegBiryani.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblVegBiryani.setBounds(40, 178, 147, 29);
		panel.add(lblVegBiryani);
		
		jburger = new JTextField();
		jburger.setHorizontalAlignment(SwingConstants.RIGHT);
		jburger.setBounds(341, 56, 147, 20);
		panel.add(jburger);
		jburger.setColumns(10);
		
		jcheese = new JTextField();
		jcheese.setHorizontalAlignment(SwingConstants.RIGHT);
		jcheese.setColumns(10);
		jcheese.setBounds(341, 90, 147, 20);
		panel.add(jcheese);
		
		jpizza = new JTextField();
		jpizza.setHorizontalAlignment(SwingConstants.RIGHT);
		jpizza.setColumns(10);
		jpizza.setBounds(341, 125, 147, 20);
		panel.add(jpizza);
		
		jcheesepizza = new JTextField();
		jcheesepizza.setHorizontalAlignment(SwingConstants.RIGHT);
		jcheesepizza.setColumns(10);
		jcheesepizza.setBounds(341, 157, 147, 20);
		panel.add(jcheesepizza);
		
		jbiryani = new JTextField();
		jbiryani.setHorizontalAlignment(SwingConstants.RIGHT);
		jbiryani.setColumns(10);
		jbiryani.setBounds(341, 187, 147, 20);
		panel.add(jbiryani);
		
		JLabel lblMeals = new JLabel("Meals");
		lblMeals.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblMeals.setBounds(213, 22, 65, 29);
		panel.add(lblMeals);	
		JPanel panel_1 = new JPanel();
		panel_1.setBorder(new LineBorder(new Color(0, 0, 0), 8));
		panel_1.setBounds(578, 149, 383, 218);
		frame.getContentPane().add(panel_1);
		panel_1.setLayout(null);
		
		JLabel lblCoke = new JLabel("Coke");
		lblCoke.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblCoke.setBounds(25, 47, 147, 29);
		panel_1.add(lblCoke);
		
		JLabel lblColdCoffee = new JLabel("Cold Coffee");
		lblColdCoffee.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblColdCoffee.setBounds(25, 81, 147, 29);
		panel_1.add(lblColdCoffee);
		
		JLabel lblFanta = new JLabel("Banana Shake");
		lblFanta.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblFanta.setBounds(25, 116, 147, 29);
		panel_1.add(lblFanta);
		
		JLabel lblLimca = new JLabel("Limca");
		lblLimca.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblLimca.setBounds(25, 148, 147, 29);
		panel_1.add(lblLimca);
		
		JLabel lblChocolateShake = new JLabel("Chocolate Shake");
		lblChocolateShake.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblChocolateShake.setBounds(25, 178, 166, 29);
		panel_1.add(lblChocolateShake);
		
		jcoke = new JTextField();
		jcoke.setHorizontalAlignment(SwingConstants.RIGHT);
		jcoke.setColumns(10);
		jcoke.setBounds(213, 56, 147, 20);
		panel_1.add(jcoke);
		
		jcoffee = new JTextField();
		jcoffee.setHorizontalAlignment(SwingConstants.RIGHT);
		jcoffee.setColumns(10);
		jcoffee.setBounds(213, 90, 147, 20);
		panel_1.add(jcoffee);
		
		jbanana = new JTextField();
		jbanana.setHorizontalAlignment(SwingConstants.RIGHT);
		jbanana.setColumns(10);
		jbanana.setBounds(213, 125, 147, 20);
		panel_1.add(jbanana);
		
		jlimca = new JTextField();
		jlimca.setHorizontalAlignment(SwingConstants.RIGHT);
		jlimca.setColumns(10);
		jlimca.setBounds(213, 157, 147, 20);
		panel_1.add(jlimca);
		
		jshake = new JTextField();
		jshake.setHorizontalAlignment(SwingConstants.RIGHT);
		jshake.setColumns(10);
		jshake.setBounds(213, 187, 147, 20);
		panel_1.add(jshake);
		
		JLabel lblDrinks = new JLabel("Drinks");
		lblDrinks.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblDrinks.setBounds(140, 21, 65, 29);
		panel_1.add(lblDrinks);
		
		JPanel panel_2 = new JPanel();
		panel_2.setBorder(new LineBorder(new Color(0, 0, 0), 8));
		panel_2.setBounds(578, 378, 383, 168);
		frame.getContentPane().add(panel_2);
		panel_2.setLayout(null);
		
		JLabel lblTax = new JLabel("Tax");
		lblTax.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblTax.setBounds(26, 24, 147, 29);
		panel_2.add(lblTax);
		
		JLabel lblSubTotal = new JLabel("Sub Total");
		lblSubTotal.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblSubTotal.setBounds(26, 64, 147, 29);
		panel_2.add(lblSubTotal);
		
		JLabel lblTotal = new JLabel("Total");
		lblTotal.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblTotal.setBounds(26, 104, 165, 29);
		panel_2.add(lblTotal);
		
		JLabel lbltax = new JLabel("");
		lbltax.setHorizontalAlignment(SwingConstants.RIGHT);
		lbltax.setBorder(new LineBorder(new Color(0, 0, 0), 2));
		lbltax.setBounds(214, 35, 147, 18);
		panel_2.add(lbltax);
		
		JLabel lblsub = new JLabel("");
		lblsub.setHorizontalAlignment(SwingConstants.RIGHT);
		lblsub.setBorder(new LineBorder(new Color(0, 0, 0), 2));
		lblsub.setBounds(214, 75, 147, 18);
		panel_2.add(lblsub);
		
		JLabel lbltotal = new JLabel("");
		lbltotal.setHorizontalAlignment(SwingConstants.RIGHT);
		lbltotal.setBorder(new LineBorder(new Color(0, 0, 0), 2));
		lbltotal.setBounds(214, 115, 147, 18);
		panel_2.add(lbltotal);
		
		JPanel panel_3 = new JPanel();
		panel_3.setBorder(new LineBorder(new Color(0, 0, 0), 8));
		panel_3.setBounds(36, 378, 524, 168);
		frame.getContentPane().add(panel_3);
		panel_3.setLayout(null);
		
		JLabel lblCostOfMeal = new JLabel("Cost of Meals");
		lblCostOfMeal.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblCostOfMeal.setBounds(46, 11, 147, 29);
		panel_3.add(lblCostOfMeal);
		
		JLabel lblCostOfDrinks = new JLabel("Cost of Drinks");
		lblCostOfDrinks.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblCostOfDrinks.setBounds(46, 51, 147, 29);
		panel_3.add(lblCostOfDrinks);
		
		JLabel lblcostd = new JLabel("Cost of Delivery");
		lblcostd.setFont(new Font("Tahoma", Font.PLAIN, 22));
		lblcostd.setBounds(46, 91, 165, 29);
		panel_3.add(lblcostd);
		
		JLabel lblmeal = new JLabel("");
		lblmeal.setHorizontalAlignment(SwingConstants.RIGHT);
		lblmeal.setBorder(new LineBorder(new Color(0, 0, 0), 2));
		lblmeal.setBounds(345, 22, 147, 18);
		panel_3.add(lblmeal);
		
		JLabel lbldrink = new JLabel("");
		lbldrink.setHorizontalAlignment(SwingConstants.RIGHT);
		lbldrink.setBorder(new LineBorder(new Color(0, 0, 0), 2));
		lbldrink.setBounds(345, 63, 147, 18);
		panel_3.add(lbldrink);
		
		JLabel lbldelivery = new JLabel("");
		lbldelivery.setHorizontalAlignment(SwingConstants.RIGHT);
		lbldelivery.setBorder(new LineBorder(new Color(0, 0, 0), 2));
		lbldelivery.setBounds(345, 103, 147, 18);
		panel_3.add(lbldelivery);
		
		JCheckBox jcdelivery = new JCheckBox("Home Delivery");
		jcdelivery.setFont(new Font("Tahoma", Font.PLAIN, 22));
		jcdelivery.setBounds(46, 127, 178, 23);
		panel_3.add(jcdelivery);
		
		JCheckBox jctax = new JCheckBox("Tax");
		jctax.setFont(new Font("Tahoma", Font.PLAIN, 22));
		jctax.setBounds(292, 128, 97, 23);
		panel_3.add(jctax);
		
		JSeparator separator = new JSeparator();
		separator.setBounds(501, 118, 1, 2);
		panel_3.add(separator);
		
		JSeparator separator_1 = new JSeparator();
		separator_1.setBounds(130, 127, 1, 2);
		panel_3.add(separator_1);
		
		JPanel panel_4 = new JPanel();
		panel_4.setBorder(new LineBorder(new Color(0, 0, 0), 8));
		panel_4.setBounds(36, 557, 1306, 82);
		frame.getContentPane().add(panel_4);
		panel_4.setLayout(null);
		
		JButton btnTotal = new JButton("Total");
		btnTotal.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				double mealtotal;
				double ncheeseburger;
				double npizza;
				double ncheesepizza;
				double nbiryani;
				double burger=30,cheeseburger=40, pizza=100, cheesepizza=150 ,biryani=60; 
				 if(jburger.getText().isEmpty())
					 nburger=0;
				 else
					 nburger=Double.parseDouble(jburger.getText());
				 if(jcheese.getText().isEmpty())
					 ncheeseburger=0;
				 else
					 ncheeseburger=Double.parseDouble(jcheese.getText());
				 if(jpizza.getText().isEmpty())
					 npizza=0;
				 else
					 npizza=Double.parseDouble(jpizza.getText());
				 if(jcheesepizza.getText().isEmpty())
					 ncheesepizza=0;
				 else
					 ncheesepizza=Double.parseDouble(jcheesepizza.getText());
				 if(jbiryani.getText().isEmpty())
					 nbiryani=0;
				 else
					 nbiryani=Double.parseDouble(jbiryani.getText());
				 
				double aburger, acheeseburger,apizza,acheesepizza,abiryani;
				aburger=burger*nburger;
				acheeseburger=cheeseburger*ncheeseburger;
				apizza=pizza*npizza;
				acheesepizza=cheesepizza*ncheesepizza;
				abiryani=biryani*nbiryani;
				mealtotal=aburger+acheeseburger+apizza+acheesepizza+abiryani;
				String pmeal=String.format("%.2f",mealtotal);
				lblmeal.setText(pmeal);
				double drinktotal;
				double coke=25,coffee=50,banana=30,shake=40 ,limca=25; 
				double ncoke;
				double ncoffee;
				double nshake;
				double nbanana;
				double nlimca;
				
		       if(jcoke.getText().isEmpty())
				  ncoke=0;
				else
					 ncoke=Double.parseDouble(jcoke.getText());
					
			     if(jcoffee.getText().isEmpty())
					ncoffee=0;
			     else
			    	 ncoffee=Double.parseDouble(jcoffee.getText()); 
				if (jshake.getText().isEmpty())
					nshake=0;
				else
					 nshake=Double.parseDouble(jshake.getText());
				if(jbanana.getText().isEmpty())
					nbanana=0;
				else
					nbanana=Double.parseDouble(jbanana.getText());
				if(jlimca.getText().isEmpty())
					nlimca=0;
				else
					nlimca=Double.parseDouble(jlimca.getText());
				double acoke, acoffee,abanana,ashake,alimca;
				acoke=coke*ncoke;
				alimca=limca*nlimca;
				ashake=shake*nshake;
				abanana=banana*nbanana;
				acoffee=coffee*ncoffee;
				drinktotal=acoke+alimca+abanana+ashake+acoffee;
			  String pdrink=String.format("%.2f",drinktotal); 
				lbldrink.setText(pdrink);
				double idelivery=40;
				if(jcdelivery.isSelected())
				{
					String delivery=String.format("%.2f",idelivery);
					lbldelivery.setText(delivery);
				}
				else
					lbldelivery.setText("0");
				double delivery=Double.parseDouble(lbldelivery.getText());
				double total=mealtotal+drinktotal+delivery;
				double tax=((total)*18)/100;
				double alltotal=0;
				if(jctax.isSelected())
				{
					String itotal=String.format("%.2f",tax);
					lbltax.setText(itotal);
					 alltotal=total+tax;
				}
				else
				{
					lbltax.setText("0");
					alltotal=total;
				}
				double subtotal=total;
				String isubtotal=String.format("%.2f",subtotal);
				lblsub.setText(isubtotal);
				String ialltotal=String.format("%.2f",alltotal);
				lbltotal.setText(ialltotal);
				
					
			}
		});
		btnTotal.setFont(new Font("Tahoma", Font.PLAIN, 22));
		btnTotal.setBounds(345, 27, 113, 23);
		panel_4.add(btnTotal);
		
		JButton btnRec = new JButton("Receipt");
		btnRec.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			double qty1=Double.parseDouble(lblCheeseBurger.getText());
			double qty2=Double.parseDouble(lblCheeseBurger_1.getText());
			double qty3=Double.parseDouble(lblVegPizza.getText());
			double qty4=Double.parseDouble(lblCheesePizza.getText());
			double qty5=Double.parseDouble(lblVegBiryani.getText());
			double qty6=Double.parseDouble(lblCoke.getText());
			double qty7=Double.parseDouble(lblColdCoffee.getText());
			double qty8=Double.parseDouble(lblFanta.getText());
			double qty9=Double.parseDouble(lblLimca.getText());
			double qty10=Double.parseDouble(lblChocolateShake.getText());
			
			textField_6.setText("Restaurant Management System") ;
			}
			});
		
			
		btnRec.setFont(new Font("Tahoma", Font.PLAIN, 22));
		btnRec.setBounds(492, 27, 113, 23);
		panel_4.add(btnRec);
		
		JButton btnReset = new JButton("Reset");
		btnReset.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			 jburger.setText(null);
			 jcheese.setText(null);
			 jpizza.setText(null);
			 jcheesepizza.setText(null);
			 jbiryani.setText(null);
			 jcoke.setText(null);
			 jcoffee.setText(null);
		     jbanana.setText(null);
		     jlimca.setText(null);
			 jshake.setText(null);
			 lblmeal.setText(null);
			 lbldrink.setText(null);
			 lbldelivery.setText(null);
			 lbltax.setText(null);
			 lblsub.setText(null);
			 lbltotal.setText(null);
			 
			}
		});
		btnReset.setFont(new Font("Tahoma", Font.PLAIN, 22));
		btnReset.setBounds(640, 27, 113, 23);
		panel_4.add(btnReset);
		
		JButton btnExit = new JButton("Exit");
		btnExit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
		});
		btnExit.setFont(new Font("Tahoma", Font.PLAIN, 22));
		btnExit.setBounds(793, 27, 113, 23);
		panel_4.add(btnExit);
		
		JPanel panel_5 = new JPanel();
		panel_5.setBorder(new LineBorder(new Color(0, 0, 0), 8));
		panel_5.setBounds(971, 147, 371, 399);
		frame.getContentPane().add(panel_5);
		panel_5.setLayout(null);
		
		JTabbedPane tabbedPane = new JTabbedPane(JTabbedPane.TOP);
		tabbedPane.setBounds(28, 21, 333, 367);
		panel_5.add(tabbedPane);
		
		JPanel panel_6 = new JPanel();
		tabbedPane.addTab("Reciept", null, panel_6, null);
		panel_6.setLayout(null);
		
		textField_6 = new JTextField();
		textField_6.setBounds(10, 11, 318, 317);
		panel_6.add(textField_6);
		textField_6.setColumns(0);
		
		JPanel panel_7 = new JPanel();
		tabbedPane.addTab("Calculator", null, panel_7, null);
		panel_7.setLayout(null);
		
		txtDisplay = new JTextField();
		txtDisplay.setHorizontalAlignment(SwingConstants.RIGHT);
		txtDisplay.setBounds(52, 1, 237, 33);
		txtDisplay.setColumns(10);
		
	    btnr = new JButton("<-");
		btnr.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String backspace = null;
				if(txtDisplay.getText().length()>0){
					StringBuilder strb= new StringBuilder(txtDisplay.getText());
					strb.deleteCharAt(txtDisplay.getText().length()-1);
					backspace = strb.toString();
					txtDisplay.setText(backspace);
				}
			}
		});
		btnr.setFont(new Font("Tahoma", Font.BOLD, 20));
		btnr.setBounds(52, 40, 60, 60);
		
		btnC = new JButton("C");
		btnC.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				txtDisplay.setText(null);
			}
		});
		btnC.setFont(new Font("Tahoma", Font.BOLD, 20));
		btnC.setBounds(111, 40, 60, 60);
		
		btnmod = new JButton("%");
		btnmod.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				firstnum= Double.parseDouble(txtDisplay.getText());
				txtDisplay.setText("");
				operations= "%";
			}
		});
		btnmod.setFont(new Font("Tahoma", Font.BOLD, 20));
		btnmod.setBounds(170, 40, 60, 60);
		
		btna = new JButton("+");
		btna.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				firstnum= Double.parseDouble(txtDisplay.getText());
				txtDisplay.setText("");
				operations= "+";
			}
		});
		btna.setFont(new Font("Tahoma", Font.BOLD, 20));
		btna.setBounds(229, 40, 60, 60);
		
		btn7 = new JButton("7");
		btn7.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				String EnterNumber = txtDisplay.getText()+btn7.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn7.setFont(new Font("Tahoma", Font.BOLD, 20));
		btn7.setBounds(52, 98, 60, 60);
		
		btn8 = new JButton("8");
		btn8.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				String EnterNumber = txtDisplay.getText()+btn8.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn8.setFont(new Font("Tahoma", Font.BOLD, 20));
		btn8.setBounds(111, 98, 60, 60);
		
		btn9 = new JButton("9");
		btn9.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				String EnterNumber = txtDisplay.getText()+btn9.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn9.setFont(new Font("Tahoma", Font.BOLD, 20));
		btn9.setBounds(170, 98, 60, 60);
		
		btns = new JButton("-");
		btns.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				firstnum= Double.parseDouble(txtDisplay.getText());
				txtDisplay.setText("");
				operations= "-";
			}
		});
		btns.setFont(new Font("Tahoma", Font.BOLD, 20));
		btns.setBounds(229, 98, 60, 60);
		
		btn4 = new JButton("4");
		btn4.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				String EnterNumber = txtDisplay.getText()+btn4.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn4.setFont(new Font("Tahoma", Font.BOLD, 20));
		btn4.setBounds(52, 155, 60, 60);
		
		btn5 = new JButton("5");
		btn5.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				String EnterNumber = txtDisplay.getText()+btn5.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn5.setFont(new Font("Tahoma", Font.BOLD, 20));
		btn5.setBounds(111, 155, 60, 60);
		
		btn6 = new JButton("6");
		btn6.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				String EnterNumber = txtDisplay.getText()+btn6.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn6.setFont(new Font("Tahoma", Font.BOLD, 20));
		btn6.setBounds(170, 155, 60, 60);
		
		btnm = new JButton("*");
		btnm.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				firstnum= Double.parseDouble(txtDisplay.getText());
				txtDisplay.setText("");
				operations= "*";
			}
		});
		btnm.setFont(new Font("Tahoma", Font.BOLD, 20));
		btnm.setBounds(229, 155, 60, 60);
		
		btn1 = new JButton("1");
		btn1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				String EnterNumber = txtDisplay.getText()+btn1.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn1.setFont(new Font("Tahoma", Font.BOLD, 20));
		btn1.setBounds(52, 212, 60, 60);
		
		btn2 = new JButton("2");
		btn2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				String EnterNumber = txtDisplay.getText()+btn2.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn2.setFont(new Font("Tahoma", Font.BOLD, 20));
		btn2.setBounds(111, 212, 60, 60);
		
		btn3 = new JButton("3");
		btn3.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				String EnterNumber = txtDisplay.getText()+btn3.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn3.setFont(new Font("Tahoma", Font.BOLD, 20));
		btn3.setBounds(170, 212, 60, 60);
		
		btnd = new JButton("/");
		btnd.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				firstnum= Double.parseDouble(txtDisplay.getText());
				txtDisplay.setText("");
				operations= "/";
			}
		});
		btnd.setFont(new Font("Tahoma", Font.BOLD, 20));
		btnd.setBounds(229, 212, 60, 60);
		
		btn0 = new JButton("0");
		btn0.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
				String EnterNumber = txtDisplay.getText()+btn0.getText();
				txtDisplay.setText(EnterNumber);
			}
		});
		btn0.setFont(new Font("Tahoma", Font.BOLD, 20));
		btn0.setBounds(52, 268, 60, 60);
		
		btndot = new JButton(".");
		btndot.setFont(new Font("Tahoma", Font.BOLD, 20));
		btndot.setBounds(111, 268, 60, 60);
		
		btn = new JButton("+-");
		btn.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				double ops= Double.parseDouble(String.valueOf(txtDisplay.getText()));
				ops=ops*(-1);
				txtDisplay.setText(String.valueOf(ops));
			}
		});
		btn.setFont(new Font("Tahoma", Font.BOLD, 20));
		btn.setBounds(170, 268, 60, 60);
		
		btneql = new JButton("=");
		btneql.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				String answer;
				secondnum=Double.parseDouble(txtDisplay.getText());
				if(operations=="+"){
					result=firstnum+secondnum;
					answer=String.format("%.2f",result);
					txtDisplay.setText(answer);
				}
				else if(operations=="-"){
					result=firstnum - secondnum;
					answer=String.format("%.2f",result);
					txtDisplay.setText(answer);
				}
				else if(operations=="*"){
					result=firstnum *secondnum;
					answer=String.format("%.2f",result);
					txtDisplay.setText(answer);
				}
				else if(operations=="/"){
					result=firstnum /secondnum;
					answer=String.format("%.2f",result);
					txtDisplay.setText(answer);
				}
				else if(operations=="%"){
					result=firstnum%secondnum;
					answer=String.format("%.2f",result);
					txtDisplay.setText(answer);
				}
			}
				});
		btneql.setFont(new Font("Tahoma", Font.BOLD, 20));
		btneql.setBounds(229, 268, 60, 60);
		panel_7.add(txtDisplay);
		panel_7.add(btnC);
		panel_7.add(btnmod);
		panel_7.add(btna);
		panel_7.add(btn7);
		panel_7.add(btn8);
		panel_7.add(btn9);
		panel_7.add(btns);
		panel_7.add(btn4);
		panel_7.add(btn5);
		panel_7.add(btn6);
		panel_7.add(btnm);
		panel_7.add(btn1);
		panel_7.add(btn2);
		panel_7.add(btn3);
		panel_7.add(btnd);
		panel_7.add(btn0);
		panel_7.add(btndot);
		panel_7.add(btn);
		panel_7.add(btneql);
		panel_7.add(btnr);
		
		JLabel lblNewLabel = new JLabel("Restaurant Management System");
		lblNewLabel.setFont(new Font("Tahoma", Font.BOLD, 75));
		lblNewLabel.setBounds(36, 11, 1306, 120); 
		frame.getContentPane().add(lblNewLabel);
	}
}
