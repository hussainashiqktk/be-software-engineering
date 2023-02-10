import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTextField;

public class MD5HashCalculator extends JFrame implements ActionListener {
    private JTextField inputTextField;
    private JButton calculateButton;
    private JLabel resultLabel;

    public MD5HashCalculator() {
        setLayout(null);
        inputTextField = new JTextField();
        inputTextField.setBounds(10, 10, 300, 30);
        add(inputTextField);

        calculateButton = new JButton("Calculate");
        calculateButton.setBounds(10, 50, 100, 30);
        calculateButton.addActionListener(this);
        add(calculateButton);

        resultLabel = new JLabel();
        resultLabel.setBounds(10, 90, 300, 30);
        add(resultLabel);

        setTitle("MD5 Hash Calculator");
        setSize(320, 180);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
    }

    public static void main(String[] args) {
        new MD5HashCalculator().setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == calculateButton) {
            String input = inputTextField.getText();
            if (input.isEmpty()) {
                JOptionPane.showMessageDialog(this, "Input is empty");
                return;
            }

            try {
                MessageDigest md = MessageDigest.getInstance("MD5");
                byte[] messageDigest = md.digest(input.getBytes());
                BigInteger number = new BigInteger(1, messageDigest);
                String hashtext = number.toString(16);
                while (hashtext.length() < 32) {
                    hashtext = "0" + hashtext;
                }
                resultLabel.setText("MD5 hash: " + hashtext);
            } catch (NoSuchAlgorithmException ex) {
                JOptionPane.showMessageDialog(this, "Error: " + ex.getMessage());
            }
        }
    }
}
