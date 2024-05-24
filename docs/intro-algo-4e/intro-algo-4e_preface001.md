前言

不久之前，几乎只有计算机科学家或数学家听说过“算法”这个词。然而，随着计算机在我们现代生活中变得普及，这个术语不再是神秘的。如果您环顾家中，您会发现算法在最平凡的地方运行：您的微波炉、洗衣机，当然还有您的计算机。您要求算法为您提供建议：您可能喜欢什么音乐或��驶时应该选择哪条路线。我们的社会，无论好坏，都要求算法为定罪罪犯提供句子。您甚至依赖算法来保持生命，或者至少不让它杀死您：您汽车或医疗设备中的控制系统。¹“算法”这个词似乎每天都会在新闻中出现。

因此，您应该不仅仅将算法理解为计算机科学的学生或从业者，还应该将其视为世界公民。一旦您理解了算法，您就可以教育他人算法是什么，它们如何运作以及它们的局限性是什么。

本书全面介绍了现代计算机算法的研究。它呈现了许多算法，并对其进行了深入的讨论，同时使其设计对所有读者水平都可理解。所有分析都清晰地列出，有些简单，有些更复杂。我们努力保持解释清晰，同时不牺牲覆盖深度或数学严谨性。

每个章节介绍一个算法、设计技术、应用领域或相关主题。算法用英语和伪代码描述，设计为可供任何稍有编程经验的人阅读。本书包含 231 幅图表，许多图表有多个部分，展示算法的工作原理。由于我们强调*效率*作为设计标准，我们包括对算法运行时间的仔细分析。

本文主要用于本科或研究生算法或数据结构课程的教学。因为它讨论了算法设计中的工程问题，以及数学方面，所以同样适合技术专业人士自学。

在这第四版中，我们再次更新了整本书。这些变化涵盖了广泛的内容，包括新的章节和部分、彩色插图，以及我们希望您会发现更具吸引力的写作风格。

**给老师的话**

我们设计这本书既多功能又完整。您会发现它适用于各种课程，从本科数据结构课程到研究生算法课程。因为我们提供的材料远远超出了典型一个学期课程的容量，您可以选择最适合您教授的课程的材料。

您会发现很容易围绕您所需的章节来组织课程。我们设计了相对独立的章节，因此您不必担心一个章节对另一个章节的意外和不必要的依赖。在本科课程中，您可能只使用一个章节的某些部分，在研究生课程中，您可能会涵盖整个章节。

我们包含了 931 个练习和 162 个问题。每个部分都以练习结束，每个章节都以问题结束。这些练习通常是简短的问题，测试对材料的基本掌握。有些是简单的自我检查思考练习，但许多是实质性的，适合作为布置的家庭作业。问题包括更复杂的案例研究，通常引入新的内容。它们通常包含几个部分，引导学生完成解决问题所需的步骤。

与本书的第三版一样，我们已经公开了一些问题和练习的解决方案，但绝不是所有的。您可以在我们的网站[`mitpress.mit.edu/algorithms/`](http://mitpress.mit.edu/algorithms/)上找到这些解决方案。您需要查看这个网站，看看是否包含您计划分配的练习或问题的解决方案。由于我们发布的解决方案集可能随着时间的推移而增长，我们建议您每次教授课程时都检查该网站。

我们已经在适合研究生而不适合本科生的部分和练习上加了星号（★）。加星号的部分不一定比没有星号的部分更难，但可能需要对更高级的数学有一定的理解。同样，加星号的练习可能需要高级背景或超过平均水平的创造力。

**对于学生**

我们希望这本教科书为您提供了一个有趣的算法领域的入门。我们尝试使每个算法都易于理解和有趣。当您遇到陌生或困难的算法时，我们会逐步描述每个算法。我们还提供了需要理解算法分析的数学的仔细解释，并提供支持图以帮助您可视化正在发生的事情。

由于本书内容较多，您的课程可能只涵盖其中的一部分。虽然我们希望您现在将这本书作为课程教材对您有所帮助，但我们也尽力使其全面到足以值得在您未来的专业书架上占据一席之地。

阅读本书的先决条件是什么？

+   您需要一些编程经验。特别是，您应该了解递归过程和简单数据结构，如数组和链表（尽管第 10.2 节涵盖了链表和您可能会发现新的变体）。

+   您应该具备一定的数学证明能力，尤其是数学归纳法的证明。本书的一部分依赖于一些基本微积分知识。尽管本书始终使用数学，但第一部分和附录 A–D 会教会您所有需要的数学技巧。

我们的网站[`mitpress.mit.edu/algorithms/`](http://mitpress.mit.edu/algorithms/)链接到了一些问题和练习的解决方案。请随时与我们的解决方案进行对比。但是，请不要将您的解决方案发送给我们。

**对于专业人士**

本书涵盖的广泛主题使其成为一本出色的算法手册。因为每一章相对独立，您可以专注于对您最相关的主题。

由于我们讨论的大多数算法具有很强的实用性，我们会涉及实施方面的问题和其他工程问题。我们经常为那些主要是理论兴趣的少数算法提供实用的替代方案。

如果您希望实现任何算法，您应该会发现将我们的伪代码翻译成您喜欢的编程语言是一项相当简单的任务。我们设计伪代码以清晰简洁地呈现每个算法。因此，我们不涉及需要对您的编程环境做出特定假设的错误处理和其他软件工程问题。我们尝试以简单直接的方式呈现每个算法，而不允许特定编程语言的特殊性质掩盖其本质。如果您习惯于 0 起始数组，您可能会发现我们经常将数组从 1 开始索引的做法是一个小障碍。您可以始终从我们的索引中减去 1，或者只是过度分配数组并将位置 0 留空。

我们明白，如果您在课程之外使用这本书，那么您可能无法将问题和练习的解决方案与教师提供的解决方案进行对比。我们的网站，[`mitpress.mit.edu/algorithms/`](http://mitpress.mit.edu/algorithms/)，链接到一些问题和练习的解决方案，以便您检查您的工作。请不要将您的解决方案发送给我们。

**致同事**

我们提供了广泛的参考文献和指向当前文献的指针。每章结束时都附有一组章节注释，其中包含历史细节和参考资料。然而，章节注释并未提供对算法领域的完整参考。尽管这本书如此庞大，但空间限制阻止我们包含许多有趣的算法。

尽管学生们多次要求提供问题和练习的解决方案，但我们采取了不为其引用参考的政策，以防止学生诱惑自己查找解决方案而不是自己发现解决方案。

**第四版的变化**

正如我们在第二版和第三版的变化中所说的，根据您的看法，这本书要么变化不大，要么变化很大。快速查看目录表明，大多数第三版的章节和部分出现在第四版中。我们删除了三章和几个部分，但除了这些新章节外，我们还添加了三个新章节和几个新部分。

我们保留了前三版的混合组织结构。这本书不仅按问题领域组织章节，也按技术组织，融合了两者的元素。它包含基于技术的章节，如分治、动态规划、贪婪算法、摊销分析、增广数据结构、NP 完全性和近似算法。但它还有关于排序、动态集合数据结构和图问题算法的整个部分。我们发现，虽然您需要知道如何应用技术来设计和分析算法，但问题很少会告诉您哪些技术最适合解决它们。

第四版的一些变化通常适用于整本书，而有些则特定于特定章节或部分。以下是最重要的一般变化摘要：

+   我们添加了 140 个新练习和 22 个新问题。我们还改进了许多旧练习和问题，这往往是根据读者的反馈而做出的。（感谢所有提出建议的读者。）

+   我们有颜色！与麻省理工学院出版社的设计师一起，我们选择了一个有限的调色板，旨在传达信息并令人愉悦。 （我们很高兴展示红黑树的—想象一下—红色和黑色！）为了增强可读性，定义术语、伪代码注释和索引中的页码都是彩色的。

+   伪代码程序出现在棕色背景上，以便更容易识别，它们不一定出现在其第一次引用的页面上。当它们不出现时，文本会指导您到相关页面。同样，对编号方程、定理、引理和推论的非本地引用包括页面号。

+   我们删除了很少教授的主题。我们完全删除了关于斐波那契堆、范艾默·博阿斯树和计算几何的章节。此外，还删除了以下材料：最大子数组问题、指针和对象的实现、完美哈希、随机构建二叉搜索树、矩阵、用于最大流的推-重标算法、迭代快速傅里叶变换方法、线性规划中单纯形算法的细节以及整数因子分解。您可以在我们的网站上找到所有删除的材料，[`mitpress.mit.edu/algorithms/`](http://mitpress.mit.edu/algorithms/)。

+   我们审查了整本书，并重新撰写了句子、段落和章节，使写作更清晰、更个人化和性别中立。例如，以前版本中的“旅行推销员问题”现在称为“旅行推销员问题”。我们认为对于工程和科学，包括我们自己的计算机科学领域，对每个人都友好是至关重要的。（唯一让我们困扰的地方是在第十三章中，需要一个关于父母兄弟的术语。由于英语没有这样的性别中立术语，我们遗憾地坚持使用“叔叔”。）

+   章节注释、参考文献和索引已经更新，反映了自第三版以来算法领域的巨大增长。

+   我们纠正了错误，大多数更正已发布在我们第三版勘误表的网站上。那些在我们全力准备本版时报告的错误没有发布，但已在本版中进行了更正。（再次感谢所有帮助我们识别问题的读者。）

第四版的具体变化包括以下内容：

+   我们重新命名了第三章并添加了一个在深入讨论正式定义之前概述渐近符号的部分。

+   第四章经历了实质性的变化，以改善其数学基础并使其更加健壮和直观。引入了算法递归的概念，并更严格地讨论了在递归中忽略地板和天花板的主题。主定理的第二种情况包含了多对数因子，并且现在提供了主定理的“连续”版本的严格证明。我们还介绍了强大而通用的 Akra-Bazzi 方法（无需证明）。

+   第九章中的确定性顺序统计算法略有不同，并且随机化和确定性顺序统计算法的分析已经得到改进。

+   除了栈和队列，第 10.1 节还讨论了存储数组和矩阵的方法。

+   第十一章关于哈希表的内容包括对哈希函数的现代处理。它还强调了线性探测作为一种有效的方法，用于在底层硬件实现缓存以支持本地搜索时解决冲突。

+   为了取代第三版中关于矩阵的部分，我们将一个关于离线缓存的问题转换为一个完整的章节。

+   第 16.4 节现在包含了一个更直观的解释，用于分析表的加倍和减半的潜在函数。

+   第十七章关于增强数据结构已经从第三部分移至第 V 部分，反映了我们认为这种技术超越了基本材料的观点。

+   第二十五章是关于二部图中匹配的新章节。它介绍了查找最大基数匹配、解决稳定婚姻问题以及找到最大权匹配（称为“分配问题”）的算法。

+   第二十六章，关于任务并行计算，已更新为现代术语，包括章节的名称。

+   第二十七章，涵盖在线算法，是另一章新内容。在线算法中，输入是随时间到达的，而不是在算法开始时就完全可用。该章描述了几个在线算法的示例，包括确定在搭乘电梯之前等待多长时间，通过移至前端启发式方法维护链表，以及评估缓存替换策略。

+   在第二十九章中，我们删除了对单纯形算法的详细介绍，因为它过于数学密集，没有真正传达许多算法思想。该章现在侧重于如何将问题建模为线性规划，以及线性规划的基本对偶性质。

+   第 32.5 节 在字符串���配章节中增加了后缀数组的简单而强大的结构。

+   第三十三章 关于机器学习，是第三个新章节。它介绍了机器学习中使用的几种基本方法：聚类将相似项分组在一起，加权多数算法以及梯度下降找到函数的最小值。

+   第 34.5.6 节 总结了多项式时间归约的策略，以证明问题是 NP 难的。

+   第 35.3 节 中集盖问题的近似算法证明已经修订。

**网站**

您可以使用我们的网站 [`mitpress.mit.edu/algorithms/`](http://mitpress.mit.edu/algorithms/) 获取补充信息并与我们交流。该网站链接到已知错误列表、第四版中未包含的第三版材料、选定练习和问题的解决方案、本书中许多算法的 Python 实现、解释幽默教授笑话的列表（当然），以及我们可能添加的其他内容。该网站还告诉您如何报告错误或提出建议。

**我们是如何制作这本书的**

与前三版一样，第四版是用 L^AT[E]X 2*[ε]* 制作的。我们使用 Times 字体，数学公式使用 MathTime Professional II 字体排版。与所有以前的版本一样，我们使用我们编写的 C 程序 Windex 编译索引，并使用 BIBT[E]X 制作参考文献。本书的 PDF 文件是在运行 macOS 10.14 的 MacBook Pro 上创建的。

我们在第三版前言中恳求苹果更新 MacDraw Pro 以适配 macOS 10 的请求落了空，因此我们继续在运行在旧版本 macOS 10 的经典环境下的 pre-Intel Mac 上使用 MacDraw Pro 绘制插图。许多插图中出现的数学表达式是使用 psfrag 包为 L^AT[E]X 2*[ε]* 设计的。

**第四版的致谢**

自从我们在 1987 年开始写第一版以来，我们一直与麻省理工学院出版社合作，与几位主任、编辑和制作人员合作。在我们与麻省理工学院出版社的合作中，他们的支持一直非常出色。特别感谢我们的编辑玛丽·李，她忍受了我们很长时间，以及伊丽莎白·斯韦兹，她推动我们完成了这本书。还要感谢主任艾米·布兰德和亚历克斯·胡普斯。

与第三版一样，我们在制作第四版时地理位置分布，分别在达特茅斯学院计算机科学系、麻省理工学院计算机科学与人工智能实验室、麻省理工学院电气工程与计算机科学系以及哥伦比亚大学工业工程与运营研究系、计算机科学系和数据科学研究所工作。在 COVID-19 大流行期间，我们大部分时间都在家工作。我们感谢各自的大学和同事们提供如此支持和激励的环境。随着疫情似乎正在减退，我们中那些尚未退休的人迫不及待地想要回到各自的大学。

朱莉·萨斯曼，P.P.A.，再次在极大的时间压力下进行了技术性的编辑工作。如果没有朱莉，这本书将充满错误（或者说，错误会比现在多得多），并且可读性会大大降低。朱莉，我们将永远感激你。剩下的错误是作者的责任（可能是在朱莉阅读材料后插入的）。

在创建本版过程中，已纠正了以前版本中的许多错误。我们感谢我们的读者——太多了，无法列出所有——多年来他们报告了错误并提出了改进建议。

在准备本版新材料的过程中，我们得到了相当多的帮助。内维尔·坎贝尔（无从属）、MIT 的比尔·库兹莫尔和 NYU 的奇·亚普就第四章中递归处理提供了宝贵建议。加州大学河滨分校的延古在第二十六章中提供了关于并行算法的反馈。微软研究的罗布·沙皮尔通过对第三十三章中机器学习材料的详细评论改变了我们的方法。MIT 的齐琪在蒙蒂霍尔问题（问题 C-1）的分析中提供了帮助。

MIT 出版社的莫莉·西曼和玛丽·里利帮助我们选择插图中的色彩调色板，达特茅斯学院的沃伊切赫·雅罗斯提出了对我们新上色插图的设计改进建议。已经从达特茅斯毕业的伊琛（安妮）·柯和琳达·肖帮助给插图上色，琳达还制作了许多 Python 实现，这些实现可以在本书的网站上找到。

最后，我们要感谢我们的妻子们——温迪·莱斯森、盖尔·里维斯特、丽贝卡·艾弗里以及已故的妮可·科尔门——以及我们的家人。爱我们的人的耐心和鼓励使这个项目成为可能。我们深情地将这本书献给他们。

| 托马斯·H·科尔门 | *新罕布什尔州利巴农* |
| --- | --- |
| 查尔斯·E·莱斯森 | *马萨诸塞州剑桥* |
| 罗纳德·L·里维斯特 | *马萨诸塞州剑桥* |
| 克利福德·斯坦 | *纽约州纽约* |
| *2021 年 6 月* |  |

¹ 要了解算法如何影响我们日常生活的许多方式，请参阅弗莱的书籍[162]。