### Overview

This repository provides code, exercises and implementations of popular Reinforcement Learning Algorithms.
I compiled this repo from different resources listed below to complement my learning with:
- [Reinforcement Learning: An Introduction (2nd Edition)](http://incompleteideas.net/book/RLbook2018.pdf)
- [David Silver's Reinforcement Learning Course](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)

Each folder in corresponds to one or more chapters of the above textbook and/or course. In addition to exercises and solution, each folder also contains a list of learning goals, a brief concept summary, and links to the relevant readings.

```bash
tylertaewook/RLpractice
├── 1. MDP
│   └── gym_test.py 
├── 2. Dynamic Programming
│   ├── Gamblers Problem.ipynb 
│   ├── Policy Evaluation.ipynb 
│   ├── Policy Iteration.ipynb 
│   └── Value Iteration.ipynb 
├── 3. Monte Carlo
│   ├── Blackjack Playground.ipynb
│   ├── MC Control with Epsilon-Greedy Policies.ipynb
│   ├── MC Prediction.ipynb
│   └── Off-Policy MC Control with Weighted Importance Sampling.ipynb
├── 4. Temporal Difference
│   ├── Cliff Environment Playground.ipynb
│   ├── Q-Learning.ipynb
│   ├── SARSA.ipynb
│   └── Windy Gridworld Playground.ipynb
├── DQN
│   ├── Breakout Playground.ipynb
│   ├── Deep Q Learning.ipynb
│   └── dqn.py
├── Function Approximation
│   ├── MountainCar Playground.ipynb
│   └── Q-Learning with Value Function Approximation.ipynb
├── LICENSE
├── Policy Gradient
│   ├── CliffWalk Actor Critic Solution.ipynb
│   ├── CliffWalk REINFORCE with Baseline Solution.ipynb
│   ├── Continuous MountainCar Actor Critic Solution.ipynb
│   ├── README.md
│   └── a3c
├── Pytorch
│   ├── CNN-Transfer.ipynb
│   ├── CNN-advanced.ipynb
│   ├── CNN.ipynb
│   ├── DNN.ipynb
│   ├── GAN.ipynb
│   ├── PyTorch Tutorial.ipynb 
│   ├── Tutorial_Autograd.ipynb 
│   ├── Tutorial_DQN.ipynb 
│   ├── Tutorial_Dataloader.ipynb 
│   ├── Tutorial_Model.ipynb 
│   ├── Tutorial_Optimization SaveLoading model.ipynb 
│   ├── Tutorial_Savemodel.ipynb 
│   ├── Tutorial_Tensors.ipynb 
├── README.md
```

### Resources

RL
- [dennybritz/reinforcement-learning](https://github.com/dennybritz/reinforcement-learning/)
- [fg91/Deep-Q-Learning](https://github.com/fg91/Deep-Q-Learning)

PyTorch
- [Yangyangii/pytorch-practice](https://github.com/Yangyangii/pytorch-practice/)
- [vahidk/EffectivePyTorch](https://github.com/vahidk/EffectivePyTorch)
- [Official Pytorch Tutorials](https://pytorch.org/tutorials/)

Master resource: https://github.com/ritchieng/the-incredible-pytorch#Tutorials

Fundamental concepts of PyTorch: https://github.com/jcjohnson/pytorch-examples

Minimal tutorial (no comments): https://github.com/vinhkhuc/PyTorch-Mini-Tutorials

After official pytorch tutorial: https://github.com/yunjey/pytorch-tutorial


### List of Implemented Algorithms

- [Dynamic Programming Policy Evaluation](DP/Policy%20Evaluation%20Solution.ipynb)
- [Dynamic Programming Policy Iteration](DP/Policy%20Iteration%20Solution.ipynb)
- [Dynamic Programming Value Iteration](DP/Value%20Iteration%20Solution.ipynb)
- [Monte Carlo Prediction](MC/MC%20Prediction%20Solution.ipynb)
- [Monte Carlo Control with Epsilon-Greedy Policies](MC/MC%20Control%20with%20Epsilon-Greedy%20Policies%20Solution.ipynb)
- [Monte Carlo Off-Policy Control with Importance Sampling](MC/Off-Policy%20MC%20Control%20with%20Weighted%20Importance%20Sampling%20Solution.ipynb)
- [SARSA (On Policy TD Learning)](TD/SARSA%20Solution.ipynb)
- [Q-Learning (Off Policy TD Learning)](TD/Q-Learning%20Solution.ipynb)
- [Q-Learning with Linear Function Approximation](FA/Q-Learning%20with%20Value%20Function%20Approximation%20Solution.ipynb)
- [Deep Q-Learning for Atari Games](DQN/Deep%20Q%20Learning%20Solution.ipynb)
- [Double Deep-Q Learning for Atari Games](DQN/Double%20DQN%20Solution.ipynb)
- Deep Q-Learning with Prioritized Experience Replay (WIP)
- [Policy Gradient: REINFORCE with Baseline](PolicyGradient/CliffWalk%20REINFORCE%20with%20Baseline%20Solution.ipynb)
- [Policy Gradient: Actor Critic with Baseline](PolicyGradient/CliffWalk%20Actor%20Critic%20Solution.ipynb)
- [Policy Gradient: Actor Critic with Baseline for Continuous Action Spaces](PolicyGradient/Continuous%20MountainCar%20Actor%20Critic%20Solution.ipynb)
- Deterministic Policy Gradients for Continuous Action Spaces (WIP)
- Deep Deterministic Policy Gradients (DDPG) (WIP)
- [Asynchronous Advantage Actor Critic (A3C)](PolicyGradient/a3c)

