from collections.abc import Callable
from pathlib import Path

from rsw_ai.api.create_circle_dataset import create_circle_dataset
from rsw_ai.backend.generate_unique_filename import generate_unique_filename


class DatasetGenerator:
    _DEFAULT_GENERATE_COLOR_ALGORITHM = staticmethod(
        lambda param_a: (param_a % 256, param_a * 2 % 256, param_a * 3 % 256)
    )
    _DEFAULT_GENERATE_COORDINATE_ALGORITHM = staticmethod(
        lambda param_a: (param_a, param_a * 2)
    )  # 1 param, return tuple[int, int]
    _DEFAULT_GENERATE_FILENAME_ALGORITHM = staticmethod(
        generate_unique_filename
    )  # 1 param

    def __init__(self):
        # Image
        self.image_width = 500
        self.image_height = 500
        self.image_background_color = (255, 255, 255)

        # Object
        self.object_center = (250, 250)
        self.object_width = 100
        self.object_height = 100
        self.object_color = (0, 0, 0)

        # Default algorithm
        self.algorithm = lambda value: value
        self.generate_color_algorithm = (
            self._DEFAULT_GENERATE_COLOR_ALGORITHM
        )  # return: tuple(int, int, int)
        self.generate_coordinate_algorithm = (
            self._DEFAULT_GENERATE_COORDINATE_ALGORITHM
        )  # return: tuple(int, int)
        self.generate_filename_algorithm = self._DEFAULT_GENERATE_FILENAME_ALGORITHM  #

    def _value(
        self,
        value,
        default_algorithm,
        param_a: int,  # dynamic
    ):
        """
        Resolve a parameter value.

        Resolution order:
        1. None     → default_algorithm(index)
        2. method   → method(index)
        3. value    → value

        Parameters
        ----------
        value : Any
            Fixed value, callable, or None.

        default : Any
            Default parameter value.

        algorithm : Callable | None
            Default algorithm used when ``value`` is None.

        Returns
        -------
        Any
            Resolved parameter.
        """

        if value is None:
            return default_algorithm(param_a)

        if callable(value):
            return value(param_a)

        return value

    def create_circle_dataset(
        self,
        image_filename: str = "circle.png",
        metadata_filename: str = "circle.json",
        count: int = 1,
        width: int | Callable | None = 500,
        height: int | Callable | None = 500,
        center: tuple[int, int] | Callable | None = None,
        radius: int | Callable | None = None,
        circle_color: tuple[int, int, int] | Callable | None = None,
        background_color: tuple[int, int, int] | Callable | None = (255, 255, 255),
        thickness: int | Callable | None = None,
    ) -> None:
        """
        Generate one or more circle dataset samples.

        Each configurable parameter accepts one of three forms:

        - Fixed value
            Use the provided value for every generated sample.

        - Callable
            Called with the current dynamic parameter (for example,
            the sample index) and should return the value.

        - None
            Use the generator's default algorithm (``self.algorithm``)
            with the corresponding default value.


        Parameters
        ----------
        image_filename : str
            Base filename for generated outputs.

            The metadata filename is generated automatically
            by replacing the extension with ``.json``.

        count : int
            Number of samples to generate.

        width : int | Callable | None
            Image width.

        height : int | Callable | None
            Image height.

        center : tuple[int, int] | Callable | None
            Circle center.

        radius : int | Callable | None
            Circle radius.

        circle_color : tuple[int, int, int] | Callable | None
            Circle color in BGR.

        background_color : tuple[int, int, int] | Callable | None
            Background color in BGR.

        thickness : int | Callable | None
            Circle border thickness.
            Use ``-1`` to generate a filled circle.


        """

        for index in range(count):
            current_filename = generate_unique_filename(image_filename)

            current_metadata_filename = generate_unique_filename(metadata_filename)

            current_width = self._value(
                width, param_a=index, default_algorithm=self.algorithm
            )

            current_height = self._value(
                height, param_a=index, default_algorithm=self.algorithm
            )

            current_center = self._value(
                center,
                param_a=index,
                default_algorithm=self.generate_coordinate_algorithm,
            )

            current_radius = self._value(
                radius, param_a=index, default_algorithm=self.algorithm
            )

            current_circle_color = self._value(
                circle_color,
                param_a=index,
                default_algorithm=self.generate_color_algorithm,
            )

            current_background_color = self._value(
                background_color,
                param_a=index,
                default_algorithm=self.generate_color_algorithm,
            )

            current_thickness = self._value(
                thickness, param_a=index, default_algorithm=self.algorithm
            )

            create_circle_dataset(
                image_filename=current_filename,
                metadata_filename=current_metadata_filename,
                width=current_width,
                height=current_height,
                center=current_center,
                radius=current_radius,
                circle_color=current_circle_color,
                background_color=current_background_color,
                thickness=current_thickness,
            )

    def reset_algorithm(self):
        """
        Reset all algorithms to the default identity algorithm.
        """

        self.algorithm = lambda value: value
        self.generate_color_algorithm = self._DEFAULT_GENERATE_COLOR_ALGORITHM
        self.generate_coordinate_algorithm = self._DEFAULT_GENERATE_COORDINATE_ALGORITHM
        self.generate_filename_algorithm = self._DEFAULT_GENERATE_FILENAME_ALGORITHM
