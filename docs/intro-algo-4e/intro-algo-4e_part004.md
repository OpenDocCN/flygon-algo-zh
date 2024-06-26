**第四部分    高级设计和分析技术**  

**介绍**

本部分涵盖了设计和分析高效算法中使用的三种重要技术：动态规划（第十四章）、贪婪算法（第十五章）和摊销分析（第十六章）。之前的部分介绍了其他广泛适用的技术，如分治、随机化以及如何解决递归关系。本部分的技术略微复杂，但你将能够使用它们解决许多计算问题。本部分介绍的主题将在本书的后续部分再次出现。

动态规划通常适用于优化问题，其中您需要做一系列选择以得到最优解，每个选择生成与原始问题相同形式的子问题，并且相同的子问题会反复出现。关键策略是存储每个这种子问题的解，而不是重新计算它。第十四章展示了这个简单思想有时可以将指数时间算法转化为多项式时间算法。

贪婪算法通常适用于优化问题，其中您需要做一系列选择以得到最优解。贪婪算法的思想是以局部最优的方式做出每个选择，从而比动态规划得到更快的算法。第十五章将帮助您确定何时使用贪婪方法。  

摊销分析技术适用于执行一系列类似操作的某些算法。与单独限制每个操作的实际成本不同，摊销分析提供了整个序列的实际成本的最坏情况界限。这种方法的一个优势是，尽管某些操作可能很昂贵，但许多其他操作可能很便宜。在设计算法时，您可以使用摊销分析，因为算法的设计和运行时间分析通常紧密相连。第十六章介绍了对算法进行摊销分析的三种方法。  
