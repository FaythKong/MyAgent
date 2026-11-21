# 深度优先搜索（DFS）

一个使用 Python 实现的图深度优先搜索示例。算法从指定起点开始，沿着一条路径尽可能深入，再回溯访问其他分支；`visited` 集合可避免环导致重复访问。

## 运行

需要 Python 3.9 或更高版本：

```bash
python dfs.py
```

示例输出：

```text
DFS traversal: A -> B -> D -> E -> F -> C
```

## 使用

图使用邻接表表示，节点可以是任何可哈希对象：

```python
from dfs import depth_first_search

graph = {
    "start": ["left", "right"],
    "left": ["end"],
    "right": ["end"],
    "end": [],
}

print(depth_first_search(graph, "start"))
```

函数返回从起点可到达的节点列表。时间复杂度为 `O(V + E)`，空间复杂度为 `O(V)`（不计输入图）。
