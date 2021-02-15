import java.math.BigInteger;
import java.security.Key;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

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

class ProductOfRedNodesVisitor extends TreeVis{
    private final int modulus = (int) (Math.pow(10, 9)+ 7);
    private BigInteger product = new BigInteger("1");
    
    public int getResult(){
        return Integer.parseInt(product.mod(new BigInteger(Integer.toString(modulus))).toString(10));
    }

    public void visitNode(TreeNode node){
        if(node.getColor() == Color.RED){
            product = product.multiply(new BigInteger(Integer.toString(node.getValue())));
        }
        
    }

    public void visitLeaf(TreeLeaf node){
       if(node.getColor() == Color.RED){
           product = product.multiply(new BigInteger(Integer.toString(node.getValue())));
       }

    }

}

class FancyVisitor extends TreeVis{
    int part1=0, part2=0;

    public int getResult(){
            return Math.abs(part1-part2);
    }

    public void visitNode(TreeNode node){
        if(node.getDepth()%2==0){
            part1+=node.getValue();
        }        
    }

    public void visitLeaf(TreeLeaf leaf){
        if(leaf.getColor() == Color.GREEN){
            part2 += leaf.getValue();
        }
    }

}

public class JavaVisitorPattern {


    public static Tree solve(){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nodeValue = new int[n];
        int[] color = new int[n];
        Map<Integer, Set<Integer>> connections = new HashMap<>();
        Map<Integer, Integer> depth = new HashMap<>();
        fill(sc, n, nodeValue, color, connections, depth);
        return buildTree(nodeValue, color, connections, depth);
    }

    private static Tree buildTree(int[] nodeValue, int[] color, Map<Integer, Set<Integer>> connections,
                                    Map<Integer, Integer> depth) {
        Map<Integer, Tree> nodeLisMap = new HashMap<>();

        for(int i=1;i<=nodeValue.length;i++){
            addNodeBasedOnType(nodeLisMap, i, isParentNode(connections, i) ,
                                 nodeValue[i-1], Color.values()[color[i-1]], depth.get(i));            
        }
        for(int node: connections.keySet()){
            for(int connectedNode : connections.get(node)){
                if(depth.get(connectedNode)>depth.get(node)){
                    TreeNode parentNode = (TreeNode) nodeLisMap.get(node);
                    parentNode.addChild(nodeLisMap.get(connectedNode));
                }
            }
        }

        return nodeLisMap.get(1);
    }    
    private static boolean isParentNode(Map<Integer, Set<Integer>> connections, int i) {
        if(connections.get(i).size()>1 || i ==1){
            return true;
        }else{
            return false;
        }
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
                                Map<Integer, Set<Integer>> connections, Map<Integer, Integer> depth){
        
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
                Set<Integer> children = new HashSet<>();
                children.add(child);
                connections.put(parent,children);
            }
            if(connections.containsKey(child)){
                connections.get(child).add(parent);
            }else{
                Set<Integer> children = new HashSet<>();
                children.add(parent);
                connections.put(child,children);
            }
        }
        depth.put(1, 0);
        int currentDepth = 1;
        Set<Integer> nextDepth = connections.get(1);
        while(depth.keySet().size() != n){
            Set<Integer> tempSet = new HashSet<>();
            for(int node:nextDepth){
                depth.put(node, currentDepth);
                tempSet.addAll(connections.get(node));
            }
            currentDepth++;
            tempSet.removeAll(depth.keySet());
            nextDepth = tempSet;

        }
    }
    public static void main(String[] args) {
        Tree root = solve();
		SumInLeavesVisitor vis1 = new SumInLeavesVisitor();
      	ProductOfRedNodesVisitor vis2 = new ProductOfRedNodesVisitor();
      	FancyVisitor vis3 = new FancyVisitor();

      	root.accept(vis1);
      	root.accept(vis2);
      	root.accept(vis3);

      	int res1 = vis1.getResult();
      	int res2 = vis2.getResult();
      	int res3 = vis3.getResult();

      	System.out.println(res1);
     	System.out.println(res2);
    	System.out.println(res3);
    }
    
}
