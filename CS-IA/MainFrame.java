import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;

public class MainFrame extends JFrame implements ActionListener {

    JButton button = new JButton("Choose A File");
    JMenuBar menu;
    JLabel label;

    MainFrame() {
        button.setBounds(150, 200, 200, 100);
        menu = new JMenuBar();
        label = new JLabel();
        label.setBackground(Color.BLACK);
        label.setFont(label.getFont().deriveFont(15.0f));
        label.setHorizontalAlignment(SwingConstants.LEFT);
        label.setBounds(0, -100, 500,500);
        label.setText("Instructions:\n" +
                "Choose An Excel File to Perform Analysis On");
        this.setSize(500, 400);
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        this.add(button);
        this.setJMenuBar(menu);
        this.setLayout(null);
        this.setVisible(true);
        this.add(label);

        button.addActionListener(this);

    }

    public static void main(String[] args) {
        new MainFrame();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == button){

            JFileChooser fileChooser = new JFileChooser();

            fileChooser.setCurrentDirectory(new File("."));

            //int response = fileChooser.showOpenDialog(null);
            int response = fileChooser.showSaveDialog(null);

            if (response == JFileChooser.APPROVE_OPTION) {
                File file = new File(fileChooser.getSelectedFile().getAbsolutePath());
                System.out.println(file);

            }
        }
    }
}
