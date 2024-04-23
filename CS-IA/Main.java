import java.awt.*;
import java.io.*;
import java.util.*;
import javax.swing.*;
import javax.swing.table.*;
import com.opencsv.*;

public class Main {
    public static void main(String[] args) {

        Vector<String> headers = new Vector<>();
        Vector<Vector<String>> data = new Vector<>();

        File file = new File("StressLevelDataset.csv");
        JButton button = new JButton("Predict N/A Data");
        JPanel panel;

        try {

            FileReader filereader = new FileReader(file);
            CSVReader csvReader = new CSVReader(filereader);
            String[] nextRecord;
            boolean firstRow = true;
            while ((nextRecord = csvReader.readNext()) != null) {
                if (firstRow) {
                    for (String cell : nextRecord) {
                        headers.add(cell);
                    }
                    firstRow = false;
                } else {
                    Vector<String> row = new Vector<>();
                    for (String cell : nextRecord) {
                        row.add(cell);
                    }
                    data.add(row);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        ImageIcon NN = new ImageIcon("C:\\Users\\lenovo\\IdeaProjects\\IA\\src\\NN.png");
        ImageIcon Graph = new ImageIcon("C:\\Users\\lenovo\\IdeaProjects\\IA\\src\\Gr.png");
        ImageIcon Dump = new ImageIcon("C:\\Users\\lenovo\\IdeaProjects\\IA\\src\\DEL.jpg");
        ImageIcon Fil = new ImageIcon("C:\\Users\\lenovo\\IdeaProjects\\IA\\src\\Filter.png");

        panel = new JPanel();
        panel.setLayout(null);
        panel.setBounds(500, 0, 500, 1000);
        panel.setBackground(Color.BLACK);

        button.setFocusable(false);
        button.setBounds(40, 20, 186, 170);
        button.setIcon(NN);
        button.setHorizontalTextPosition(SwingConstants.CENTER);
        button.setVerticalTextPosition(SwingConstants.BOTTOM);
        panel.add(button);

        JButton graph = new JButton("Graph Data");
        graph.setFocusable(false);
        graph.setBounds(280, 20, 148,170);
        graph.setIcon(Graph);
        graph.setHorizontalTextPosition(SwingConstants.CENTER);
        graph.setVerticalTextPosition(SwingConstants.BOTTOM);
        panel.add(graph);

        JButton Delete = new JButton("Delete Column");
        Delete.setFocusable(false);
        Delete.setBounds(40, 210, 170, 192);
        Delete.setIcon(Dump);
        Delete.setHorizontalTextPosition(SwingConstants.CENTER);
        Delete.setVerticalTextPosition(SwingConstants.BOTTOM);
        panel.add(Delete);

        JButton Filter = new JButton("Filter Data");
        Filter.setFocusable(false);
        Filter.setBounds(250, 210, 170, 200);
        Filter.setIcon(Fil);
        Filter.setHorizontalTextPosition(SwingConstants.CENTER);
        Filter.setVerticalTextPosition(SwingConstants.BOTTOM);
        panel.add(Filter);

        JTable table = new JTable(new CustomTableModel(data, headers));

        table.setPreferredScrollableViewportSize(new Dimension(500, 500));

        JScrollPane scroll = new JScrollPane(table);

        scroll.setPreferredSize(new Dimension(500, 500));

        JFrame f = new JFrame();
        f.setSize(1000, 1000);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        f.getContentPane().setLayout(null);

        scroll.setBounds(0, 0, 500, 500);
        f.getContentPane().add(scroll);

        panel.setBounds(500, 0, 500, 1000);
        f.getContentPane().add(panel);
        f.setResizable(false);

        f.setVisible(true);

    }
}

class CustomTableModel extends DefaultTableModel {
    public CustomTableModel(Vector<Vector<String>> data, Vector<String> columnNames) {
        super(data, columnNames);
    }
}
// https://stackoverflow.com/questions/62347146/how-to-display-excel-data-in-jtable-in-java
