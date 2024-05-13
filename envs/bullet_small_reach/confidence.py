# Copyright (C) 2023. Huawei Technologies Co., Ltd. All rights reserved.

# This program is free software; you can redistribute it and/or modify it under
# the terms of the MIT license.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the MIT License for more details.



from typing import Union, Any, Dict, List, Optional, Tuple, Callable
import numpy as np


class LambdaS:
    """
    Class representing the confidence function.

    Parameters:
    ----------
    pos_tol : float, optional
        Position tolerance (default is 3.)
    """

    def __init__(self, pos_tol: float = 3.):
        self.pos_tol = pos_tol

    def get_use_local(self, env: Any, observation: List) -> float:
        """
        Get the lambda s value based on the environment and observation.

        Parameters:
        ----------
        env : Any
            The environment
        observation : list of array
            The observation.

        Returns:
        ----------
        float
            Use_local value (0 or 1).
        """
        agent_pos = env.env.env.agent.get_position()[:2]
        pos_los = [obstacle.get_position()[:2] for obstacle in env.env.obstacles]
        min_distance = np.min(np.linalg.norm(np.vstack(pos_los) - agent_pos, axis=1))
        if abs(min_distance) <= self.pos_tol:
            return 1
        return 0


def bullet_small_reach_lambda_s(expert: Any,
                                device: str = "cpu",
                                pos_tol: float = None,
                                speed_tol: float = None,
                                smoothed: bool = None) -> LambdaS:
    """
    Returns the confidence LambdaS instance for the bullet reach environment.

    Parameters:
    ----------
    expert : Any
        Expert (not used, but here in case the lambda_s depends on the expert).
    device : str, optional
        Device for computation (default is 'cpu')
    pos_tol : float or None, optional
        Position tolerance (default is None)
    speed_tol : float or None, optional
        Speed tolerance (default is None)
    smoothed : bool or None, optional
        Whether to use smoothed lambda_s (default is None)

    Returns:
    ----------
    LambdaS
        The LambdaS instance
    """
    return LambdaS()
