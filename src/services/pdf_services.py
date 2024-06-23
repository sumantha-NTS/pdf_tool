from ocrmypdf import ocr
from io import BytesIO
from PyPDF2 import PdfReader, PdfWriter
from typing import List, Any


def process_pdf_pipeline(
    file,
    image_dpi: int = None,
    deskew: bool = False,
    remove_background=False,
) -> bytes:
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


def split_pdf(pdf_file: PdfReader, pages: List[str]) -> List:
    result = []
    for page_range in pages:
        split_pages = page_range.split("-")
        if len(split_pages) == 1:
            start = int(split_pages[0])
            end = int(split_pages[0])
        elif len(split_pages) == 2:
            start = int(split_pages[0])
            end = int(split_pages[1])
        else:
            result.append(["error", f"Invalid page range: {page_range}"])
            break

        if start > len(pdf_file.pages) or end > len(pdf_file.pages):
            result.append(["error", f"Invalid page range: {page_range}"])
            break

        pdf_writer = PdfWriter()
        for page_num in range(start - 1, end):
            pdf_writer.add_page(pdf_file.pages[page_num])
        output = BytesIO()
        pdf_writer.write(output)

        result.append(["success", output.getvalue()])
    return result


def merge_pdf(file):
    pass
