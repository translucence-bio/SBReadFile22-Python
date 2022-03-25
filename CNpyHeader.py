import numpy

class CNpyHeader(object):
    """ generated source for class CNpyHeader """
    mLittleEndian = bool()
    mFortranOrder = bool()
    mShape = []
    mHeaderSize = int()
    mDataType = str()
    mBytesPerPixel = int()

    def ByteArrayToShort(self, byteArrau, offset):
        """ generated source for method ByteArrayToShort """
        theVal = ((byteArrau[offset + 1] & 0xFF) << 8) | ((byteArrau[offset + 0] & 0xFF) << 0)
        return int(theVal)

    def ByteArrayToInt(self, byteArrau, offset):
        """ generated source for method ByteArrayToInt """
        return ((byteArrau[offset + 3] & 0xFF) << 24) | ((byteArrau[offset + 2] & 0xFF) << 16) | ((byteArrau[offset + 1] & 0xFF) << 8) | ((byteArrau[offset + 0] & 0xFF) << 0)


    def ParseNpyHeader(self, inStream):
        """ generated source for method ParseNpyHeader """
        try:
            theBuffer = inStream.readline()
            self.mHeaderSize = len(theBuffer)
            inStream.seek(0)

            major, minor = numpy.lib.format.read_magic(inStream)
            self.mShape, self.mFortranOrder, self.mDataType = numpy.lib.format.read_array_header_1_0(inStream)
            if self.mDataType == 'uint16':
                self.mBytesPerPixel = 2
            else:
                print ("Invalid header")
                return False

        except :
            return False
        return True


