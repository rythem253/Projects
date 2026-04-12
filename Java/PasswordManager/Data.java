
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.beans.Statement;
import java.nio.charset.StandardCharsets;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;


public class Data implements ActionListener {

static final String DB_URL = "jdbc:mariadb://localhost:3306/testDB";
static final String USER = "rythem";
static final String PASS = "2509";

    JPasswordField passField = new JPasswordField(15);
    TextField appField = new TextField(15);
    JPanel dataPanel = new JPanel();

    public Data()
    
    {

        JFrame dataFrame = new JFrame("Database");
        dataFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        dataFrame.setSize(200,300);

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);
        gbc.fill = GridBagConstraints.HORIZONTAL;

        JLabel appName = new JLabel("App");
        gbc.gridx = 0;
        gbc.gridy = 0;
        dataPanel.add(appName);

        gbc.gridx = 1;
        dataPanel.add(appField);

        JLabel passwordJLabel = new JLabel("Password");
        gbc.gridx = 0;
        gbc.gridy = 1;
        dataPanel.add(passwordJLabel);

        gbc.gridx = 1;
        dataPanel.add(passField);

        
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.gridwidth = 2;
        JButton addButton = new JButton("Add Credentials");
        dataPanel.add(addButton);

        addButton.addActionListener(this);
    
        dataFrame.add(dataPanel);
        dataFrame.setVisible(true);   
    }

    //Gets app name.
    public String getAppName() 

    {
        return appField.getText();
    }

    public String getPassword()   

    {
        return new String(passField.getPassword());
    } 

    //When button clicked, the information is stored in the database;
    public void actionPerformed(ActionEvent e) 
    
    {
        //SQL file will be added here, where passwords are stored securely
        try {

            String temp1 = getAppName();
            String temp2 = getPassword();

            String name = temp1; ; //add name of app user wants to add;
            String password = temp2; //add password;

            Connection con = DriverManager.getConnection(DB_URL, USER, PASS);
            PreparedStatement ps = con.prepareStatement("INSERT INTO myTable (name, password) values (?, ?)");

            ps.setString(1, name);
            ps.setString(2, password);

            int i = ps.executeUpdate();

            if (i > 0) {
                System.out.println("Success");
            } else {
                System.out.println("fail");
            }
        } catch (SQLException e1) {
            e1.printStackTrace();
        }
    }
}




   

        
