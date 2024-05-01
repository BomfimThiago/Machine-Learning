With reinforcement learning, a machine learning model is trained to mimic the way animals or children learn.
Good actions are rewarded or reinforced, while bad actions are discouraged and penalized


Agente: The learner or decision-maker
Environment: Everything the agent interacts with
Action: What the agent can do
State: The current situation returned by the environment
Reward: Feedback from the environment

Analogy: Think of it as trainning a dog. The dog is the agent, the world is its environment, commands you teach are actions, the dog's current activity or situation is the state, and treats or praises are rewards.

Policy: The strategy that the agent employs to determine the next action based on the current state
Value Function: It estimates how good it is for the agent to be in a given state(or how good it is to perform a certain action in a give state)
Model of the environment: This might be used for planning, where the agent predicts what the next state and reward will be for each action.

Analogy: The policy is like a recipe that guides you through the steps(actions) to cook a dish (reach a goal state) based on what ingredients(states) you currently have in your kitchen(environment)


Reinforcement learning can primarily be divided into two types of methods:
- Model-free methods: In these methods, the agent learns to act without requiring a model of the environment. Examples include Q-learning and policy gradients
- Model-based methods: These involve the agent constructing a model of the environment to inform its decision-making, potentially leading to more efficient learning


Topics that can studied:
- Deep Reinforcement Learning: Combining deep learning with RL, using neural networks to approximate policies, value functions, or models
- Partial Observability: Dealing with scenarios where the agent can't observe the full state of the environment directly
- Mathematics: Solid foundation in probability, statistics and linear algebra will help

Key Machine Learning Concepts for RL
- Gradient Descent - this is a way to minimize an objective function - parametrized by a model's parameters - by updating the parameters in the opposite direction of the gradient of the objective function w.r.t. the parameters.
It's used in training in almost all the deep learning models.

Analogy: Imagine you're in a mountainous region covered in fog(the landscape is your error landscape, and you want to get to the lowest valley - the minimum error). You can only see your immediate surroundings.To find the lowest point, you feel the ground to discern the steepest descent and take a step in that direction