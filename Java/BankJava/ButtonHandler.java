//Class for actionListener only.

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JLabel;
import javax.swing.JOptionPane;


import javax.swing.JOptionPane;

public class ButtonHandler implements ActionListener {

    private int startingBalance = 10;
    private JLabel balanceLabel;

    public void setBalance(JLabel label) {
        this.balanceLabel = label;
    }
    
    public int getAmount() {
        return startingBalance;
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        handlingAccount(e);
    }

    public int handlingAccount(ActionEvent e) {

    String command = e.getActionCommand();  // Get which button was clicked
        
    switch (command) {

            case "Withdraw": {

                String w = JOptionPane.showInputDialog(null, "Enter the withdrawal amount: ");

                    int amount = Integer.parseInt(w);
                    if (amount > startingBalance) {
                        JOptionPane.showMessageDialog(null, "Insufficient funds!");
                        break;
                    }
                    
                    if (amount < startingBalance) {
                    balanceLabel.setText("Current balance is" + (startingBalance-=amount));
                    }
                break; 
                }
            
            case "Deposit": {

                String d = JOptionPane.showInputDialog("Enter deposit amount: ");
                int amount = Integer.parseInt(d);

                if (amount == 0) {
                    JOptionPane.showMessageDialog(null, "The amount should be greater than 0");
                } 

                startingBalance+=amount;
                balanceLabel.setText("Current balance is" + startingBalance);


                break;
            }
            
            case "Balance":
                JOptionPane.showMessageDialog(null, startingBalance);
            break;
        }

        return startingBalance;
    
    }
}
    

    