import javax.swing.*;
import javax.swing.text.html.StyleSheet;
import java.awt.*;
import java.awt.event.*;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.KeySpec;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Base64;

public class Screens implements ActionListener {

    static final String DB_URL = "jdbc:mariadb://localhost:3306/testDB";
    static final String USER = "rythem";
    static final String PASS = "2509";

    JFrame frame;
    JButton submit;
    JTextField tf1;
    JPasswordField tf2;

    private String CreatedPassword; 
    private String CreatedUsername;

    public Screens(String TransferPassword, String TransferUsername) 
    
    {
        this.CreatedPassword = TransferPassword;
        this.CreatedUsername = TransferUsername;

        frame = new JFrame("Password Manager");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Main panel with padding
        JPanel panel = new JPanel(new GridBagLayout());
        panel.setBorder(BorderFactory.createEmptyBorder(15, 15, 15, 15));

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(20, 20, 20, 20);
        gbc.fill = GridBagConstraints.HORIZONTAL;

        // Username
        gbc.gridx = 0;
        gbc.gridy = 0;
        panel.add(new JLabel("Username:"), gbc);

        gbc.gridx = 1;
        tf1 = new JTextField(15);
        panel.add(tf1, gbc);

        // Password
        gbc.gridx = 0;
        gbc.gridy = 1;
        panel.add(new JLabel("Password:"), gbc);

        gbc.gridx = 1;
        tf2 = new JPasswordField(15);
        panel.add(tf2, gbc);

        // Submit button
        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.gridwidth = 2;
        gbc.anchor = GridBagConstraints.CENTER;

        submit = new JButton("Submit");
        panel.add(submit, gbc);

        submit.addActionListener(this);

        frame.add(panel);
        frame.pack();
        frame.setLocationRelativeTo(null); // center
        frame.setVisible(true);
    }

    public String passwordToString() 
   
    {
        return new String(tf2.getPassword());
    }
    

    //Hashing+salting happens here:
    public String Cryptography() throws Exception 
    
    {
        String passString = CreatedPassword;

        SecureRandom random = new SecureRandom();
        byte[] salt = new byte[64];
        random.nextBytes(salt);

        KeySpec spec = new PBEKeySpec(passString.toCharArray(), salt, 65536, 128);
        SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        byte[] hash = factory.generateSecret(spec).getEncoded();

        String hashedPass = Base64.getEncoder().encodeToString(hash);
        String saltBase64 = Base64.getEncoder().encodeToString(salt);
        
        String combinedHashSalt = hashedPass + ":" + saltBase64;

        return combinedHashSalt;
    }
            
    public void actionPerformed(ActionEvent e) 
    
    {
        if (e.getSource() == submit) {

        try {
        
        String selectQuery = "SELECT Username, Password FROM passCheck WHERE Username = ? AND Password = ?";

        final String MasterKeyLoginUsername = tf1.getText();
        final String MasterKeyLoginPassword = passwordToString();

        Connection con = DriverManager.getConnection(DB_URL, USER, PASS);
        PreparedStatement ps = con.prepareStatement(selectQuery); //SQL Comand to select username for login.
        
        ps.setString(1, MasterKeyLoginUsername);
        ps.setString(2, MasterKeyLoginPassword);

        ResultSet rs = ps.executeQuery();

        if (rs.next()) {
            frame.dispose();
            new Data();
        } else {
            JOptionPane.showMessageDialog(null, "Username or Password Incorrect !");
        }
            } catch (SQLException e1) {
                e1.printStackTrace();
        }
        
    }}}

