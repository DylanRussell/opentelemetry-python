from abc import ABC, abstractmethod
from opentelemetry.sdk._logs.export import LogExporter
from opentelemetry.sdk.metrics.export import (
    MetricExporter,
)
from opentelemetry.sdk.trace.export import SpanExporter


# Class which can be used to customize the configurator.
class _BaseConfiguratorCustomizer(ABC):
    @abstractmethod
    def customize_log_exporter(log_exporter: LogExporter):
        pass

    @abstractmethod
    def customize_metric_exporter(metric_exporter: MetricExporter):
        pass

    @abstractmethod
    def customize_span_exporter(span_exporter: SpanExporter):
        pass
