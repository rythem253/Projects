import java.awt.*;
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;;

public class Account {

    public static void main(String[] args) {

        ButtonHandler handler = new ButtonHandler();
    
        JFrame frame = new JFrame("ABC Bank");
        frame.setSize(500, 550);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JLabel label1 = new JLabel("Welcome to ABC Bank");
        label1.setHorizontalAlignment(JLabel.CENTER);
        JLabel currBalanceLabel = new JLabel("Current Balance is: " + handler.getAmount());
        handler.setBalance(currBalanceLabel);

        currBalanceLabel.setHorizontalAlignment(JLabel.CENTER);
        frame.add(label1, BorderLayout.NORTH);
        frame.add(currBalanceLabel, BorderLayout.SOUTH);

        //Create a JPanel to hold the button
        JPanel centerPanel = new JPanel(); // default is FlowLayout (respects preferred size)

        JButton depositButton = new JButton("Deposit");
        depositButton.setPreferredSize(new Dimension(150, 50)); // Set your custom size
    
        JButton withdraw = new JButton("Withdraw");
        withdraw.setPreferredSize(new Dimension(150, 50));

        JButton viewBalance  = new JButton("Balance");
        viewBalance.setPreferredSize(new Dimension(150, 50));

        centerPanel.add(depositButton); // Add button to panel
        centerPanel.add(withdraw);
        centerPanel.add(viewBalance);

        depositButton.addActionListener(handler);
        withdraw.addActionListener(handler);
        viewBalance.addActionListener(handler);

        frame.add(centerPanel, BorderLayout.CENTER); // Add panel to frame  
        frame.setVisible(true);

        
       
    }

}
