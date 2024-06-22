from ocrmypdf import ocr
from io import BytesIO


def process_pdf_pipeline(
    file,
    image_dpi: int = None,
    deskew: bool = False,
    remove_background=False,
) -> None:
    input_pdf_stream = BytesIO(file)
    output_pdf_stream = BytesIO()

    ocr(
        input_file=input_pdf_stream,
        output_file=output_pdf_stream,
        image_dpi=image_dpi,
        deskew=deskew,
        remove_background=remove_background,
        progress_bar=True,
    )

    output_pdf_bytes = output_pdf_stream.getvalue()

    # Close the streams
    input_pdf_stream.close()
    output_pdf_stream.close()
    return output_pdf_bytes
