import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.security.SecureRandom;
import java.security.spec.KeySpec;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Base64;

public class CreateUser implements ActionListener {

    JFrame userCreateFrame;
    JButton createBtn;
    JPasswordField tfPass;
    JTextField tfUserName;
    JButton alrButton;
      
    static final String DB_URL = "jdbc:mariadb://localhost:3306/testDB";
    static final String USER = "rythem";
    static final String PASS = "2509";

    public CreateUser() 
    
    {
        class BackgroundPanel extends JPanel {

            private Image bg;

            public BackgroundPanel() {
                bg = new ImageIcon(getClass().getResource("image1.jpg")).getImage();
            }

            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                g.drawImage(bg, 0, 0, getWidth(), getHeight(), this);
            }
        }

        userCreateFrame = new JFrame("Create Account ");
        userCreateFrame.setSize(450, 350);
        userCreateFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel panel = new BackgroundPanel();
        panel.setLayout(new GridBagLayout());
        panel.setBorder(BorderFactory.createEmptyBorder(15, 15, 15, 15));

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);
        gbc.fill = GridBagConstraints.HORIZONTAL; 

        JLabel userName = new JLabel("Please enter your username");
        userName.setFont(new Font("Arial", Font.BOLD, 16));
        gbc.gridx = 0;
        gbc.gridy = 0;
        panel.add(userName, gbc);

        tfUserName = new JTextField(15);
        gbc.gridx = 1;
        panel.add(tfUserName, gbc);

        JLabel password = new JLabel("Please enter your password");
        password.setFont(new Font("Arial", Font.BOLD, 16));
        gbc.gridx = 0;
        gbc.gridy = 1;
        panel.add(password, gbc);

        tfPass = new JPasswordField(15);
        gbc.gridx = 1;
        panel.add(tfPass, gbc);

        createBtn = new JButton("Create Account");
        gbc.gridx = 1;
        gbc.gridy = 2;
        createBtn.addActionListener(this);
        panel.add(createBtn, gbc);

        alrButton = new JButton("Already Have an Account?");
        alrButton.addActionListener(this);
        gbc.gridx = 0;
        gbc.gridy = 3;
        panel.add(alrButton, gbc);

        userCreateFrame.add(panel);
        userCreateFrame.setVisible(true);
    }

    public String getPassword() {
        return new String(tfPass.getPassword());
    }

    public void actionPerformed(ActionEvent e) {

        if (e.getSource() == createBtn) {
            try {
            String password = getPassword();
            String username = tfUserName.getText();

            SecureRandom random = new SecureRandom();
            byte[] salt = new byte[64];
            random.nextBytes(salt);

            KeySpec spec = new PBEKeySpec(password.toCharArray(), salt, 65536, 128);
            SecretKeyFactory factory = SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");

            byte[] hash = factory.generateSecret(spec).getEncoded();

            String hashedPass = Base64.getEncoder().encodeToString(hash);
            String saltBase64 = Base64.getEncoder().encodeToString(salt);

            Connection con = DriverManager.getConnection(DB_URL, USER, PASS);
            PreparedStatement ps = con.prepareStatement("INSERT INTO passCheck (Username, Password, Hash, Salt) VALUES (?, ?, ?, ?)");
            
            ps.setString(4, saltBase64);
            ps.setString(3, hashedPass);
            ps.setString(1, username);
            ps.setString(2, password);

            int result = ps.executeUpdate();

            ps.close();
            con.close();

            if (result > 0) {
                JOptionPane.showMessageDialog(null, "Your account has been created successfully!");
                userCreateFrame.dispose();
                new Screens(password, username);
            } else {
                JOptionPane.showMessageDialog(null, "Account creation failed.");
            }

        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

        if (e.getSource() == alrButton) {
            userCreateFrame.dispose();
            new Screens("", "");
        }
    }   
}
