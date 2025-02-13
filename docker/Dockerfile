FROM continuumio/miniconda3 as base

COPY environment.yml ./
RUN conda update conda && \
    conda env update -f environment.yml -n base && \
    conda clean -af


FROM base as dependencies

ENV PATH="/opt/conda/bin:$PATH"
WORKDIR /opt/stactools-gedi-calval-copc
COPY --from=base /opt/conda /opt/conda
COPY pyproject.toml ./
COPY src/stactools/gedi_calval_copc/__init__.py src/stactools/gedi_calval_copc/
RUN apt-get -y -q update \
    && apt-get -y -q install build-essential \
    && rm -rf /var/lib/apt/lists/
RUN pip install .
RUN rm -r /opt/conda/lib/python3.11/site-packages/stactools/gedi_calval_copc


FROM dependencies as builder

ENV PATH="/opt/conda/bin:$PATH"
WORKDIR /opt/stactools-gedi-calval-copc
COPY --from=base /opt/conda /opt/conda
COPY pyproject.toml ./
COPY src ./src
RUN pip install -U pip \
    && pip install .
WORKDIR /
RUN rm -rf /opt/stactools-gedi-calval-copc
CMD [ "stac", "gedicalvalcopc" ]


FROM dependencies as dev-dependencies

ENV PATH="/opt/conda/bin:$PATH"
WORKDIR /opt/stactools-gedi-calval-copc
COPY --from=base /opt/conda /opt/conda
COPY pyproject.toml .
RUN pip install -e '.[dev]' \
    && git init


FROM dev-dependencies as dev-builder

ENV PATH="/opt/conda/bin:$PATH"
WORKDIR /opt/stactools-gedi-calval-copc
COPY --from=base /opt/conda /opt/conda
COPY . .
CMD [ "stac", "gedicalvalcopc" ]
