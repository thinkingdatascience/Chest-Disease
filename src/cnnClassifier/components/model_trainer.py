import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import TrainingConfig


class Training:
    def __init__(self, config: TrainingConfig) -> None:
        self.config = config

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    def get_updated_base_model(self):
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path)

    def training_validation_generator(self):

        datagenerator_kwargs = dict(rescale=1.0 / 255, validation_split=0.20)

        data_augmentation_kwargs = dict(
            rotation_range=40,
            width_shift_range=0.2,
            height_shift_range=0.2,
            horizontal_flip=True,
            vertical_flip=True,
            shear_range=0.0,
            zoom_range=0.0,
        )

        training_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs, **data_augmentation_kwargs
        )

        validation_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        # FLOW FROM DIRECTORY

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear",
        )

        if self.config.params_augmentation:
            train_datagenerator = training_datagenerator
        else:
            train_datagenerator = validation_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=False,
            **dataflow_kwargs
        )
        self.validation_generator = validation_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    def train(self):
        self.steps_per_epoch = (
            self.train_generator.samples // self.train_generator.batch_size
        )
        self.validation_steps = (
            self.validation_generator.samples // self.validation_generator.batch_size
        )

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.validation_generator,
        )

        self.save_model(path=self.config.trained_model_path, model=self.model)
