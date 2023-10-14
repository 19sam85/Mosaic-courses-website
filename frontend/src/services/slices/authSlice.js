import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { api } from '../../utils/api';

const initialState = {
  userName: null,
  userEmail: null,
  // userPassword: '',
  userPhone: null,
  userId: null,
  isSending: false,
  sendDataSucces: false,
  registerSucces: false,
  registerError: null,
};

const registerUser = createAsyncThunk('auth/registerUser', async (data) => {
  try {
    return api.postRegisterUser(data);
  } catch (err) {
    return err;
  }
});

export const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(registerUser.pending, (state) => {
      state.isSending = true;
      // state.authFailed = false;
      state.registerError = null;
    });
    builder.addCase(registerUser.fulfilled, (state, action) => {
      state.isSending = false;
      state.registerError = false;
      state.sendDataSucces = true;
      console.log(action.payload);
      state.userName = action.payload.first_name;
      state.userEmail = action.payload.email;
      state.userId = action.payload.id;
      state.userPhone = action.payload.phone;
    });
    builder.addCase(registerUser.rejected, (state, action) => {
      state.isSending = false;
      state.sendDataSucces = false;
      console.log(action);
      state.registerError = true;
      // bypass error
      // state.registerError = false;
      // state.sendDataSucces = true;
    });
    // [registerUser.pending]: (state) => {
    //   state.loading = true
    //   state.error = null
    // },
    // [registerUser.fulfilled]: (state, { payload }) => {
    //   state.loading = false
    //   state.success = true // registration successful
    // },
    // [registerUser.rejected]: (state, { payload }) => {
    //   state.loading = false
    //   state.error = payload
    // },
    // builder.addCase(getAllReviews.fulfilled, (state, action) => {
    //   state.allReviews = action.payload;
    // });

    // builder.addCase(getReviewById.fulfilled, (state, action) => {
    //   state.currentReview = action.payload;
    // });
    // builder.addCase(authRequest.fulfilled, (state, action) => {
    //   state.requestState = true;
    // });
  },
});

const authSliceReducer = authSlice.reducer;

export {
  authSliceReducer, registerUser,
};
