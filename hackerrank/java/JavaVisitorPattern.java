import java.security.Key;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

import javax.swing.text.AsyncBoxView.ChildLocator;

enum Color{
    RED, GREEN;
}
abstract class Tree{
    private int value;
    private Color color;
    private int depth;
    
    public Tree(int value, Color color, int depth){
        this.value = value;
        this.color = color;
        this.depth = depth;
    }
    
    public int getValue(){
        return this.value;
    }
    
    public Color getColor(){
        return this.color;
    }

    public int getDepth(){
        return this.depth;
    }

    public abstract void accept(TreeVis visitor);
}

class TreeNode extends Tree{
    private List<Tree> children = new ArrayList<>();
    public TreeNode(int value, Color color, int depth){
        super(value, color, depth);
    }
    
    public void accept(TreeVis visitor){
        visitor.visitNode(this);
        for(Tree child : children){
            child.accept(visitor);
        }
    }

    public void addChild(Tree node){
        this.children.add(node);
    }
}

class TreeLeaf extends Tree{
    public TreeLeaf(int value, Color color, int depth){
        super(value, color, depth);
    }

    public void accept(TreeVis visitor){
        visitor.visitLeaf(this);
    }
}

abstract class TreeVis{
    public abstract int getResult();
    public abstract void visitNode(TreeNode node);
    public abstract void visitLeaf(TreeLeaf node);
}

class SumInLeavesVisitor extends TreeVis{
    
    private int sum = 0;
    public int getResult(){
        return sum;
    }

    public void visitNode(TreeNode node){

    }

    public void visitLeaf(TreeLeaf node){
        sum += node.getValue();
    }
}


public class JavaVisitorPattern {


    public static Tree solve(){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nodeValue = new int[n];
        int[] color = new int[n];
        Map<Integer, List<Integer>> connections = new HashMap<>();

        fill(sc, n, nodeValue, color, connections);
        return buildTree(nodeValue, color, connections);
    }

    private static Tree buildTree(int[] nodeValue, int[] color, Map<Integer, List<Integer>> connections) {
        Map<Integer, Tree> nodeLisMap = new HashMap<>();

        for(int i=0;i<nodeValue.length;i++){
            int node = i+1;
            if(!nodeLisMap.containsKey(node)){
                addNodeBasedOnType(nodeLisMap, node, connections.containsKey(node),
                 nodeValue[i], Color.values()[color[i]],0);
            }
            for(int child: connections.getOrDefault(node, new ArrayList<>())){
                int index = child-1;
                addNodeBasedOnType(nodeLisMap, child, connections.containsKey(child), 
                nodeValue[index], Color.values()[color[index]], nodeLisMap.get(node).getDepth()+1);
                TreeNode parent = (TreeNode)nodeLisMap.get(node);
                parent.addChild(nodeLisMap.get(child));
            }
        }

        return nodeLisMap.get(1);
    }

    private static void addNodeBasedOnType(Map<Integer, Tree> nodeLisMap, int key, boolean isParent, int nodeValue,
            Color color, int depth) {
        if(isParent){
            nodeLisMap.put(key, new TreeNode(nodeValue, color, depth));
        }else{
            nodeLisMap.put(key, new TreeLeaf(nodeValue, color, depth));
        }
    }

    private static void fill(Scanner sc, int n, int[] nodeValue, int[] color,
                                Map<Integer, List<Integer>> connections) {
        
        for(int i=0;i<n;i++){
            nodeValue[i] = sc.nextInt();
        }
        for(int i=0;i<n;i++){
            color[i] = sc.nextInt();
        }
        while(sc.hasNext()){
            int parent = sc.nextInt();
            int child = sc.nextInt();
            if(connections.containsKey(parent)){
                connections.get(parent).add(child);
            }else{
                List<Integer> children = new ArrayList<>();
                children.add(child);
                connections.put(parent,children);
            }
        }
    }
    public static void main(String[] args) {
        Tree root = solve();
		SumInLeavesVisitor vis1 = new SumInLeavesVisitor();
      	ProductOfRedNodesVisitor vis2 = new ProductOfRedNodesVisitor();
      	// FancyVisitor vis3 = new FancyVisitor();

      	root.accept(vis1);
      	root.accept(vis2);
      	// root.accept(vis3);

      	int res1 = vis1.getResult();
      	int res2 = vis2.getResult();
      	// int res3 = vis3.getResult();

      	System.out.println(res1);
     	System.out.println(res2);
    	// System.out.println(res3);
    }
    
}
